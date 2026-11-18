#!/usr/bin/env python3
"""Offline checks for published files, portable skill metadata and local links."""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_ENDPOINT = "https://api.indexalpha.com/mcp"


def read_yaml(source: str):
    result = subprocess.run(
        ['ruby', '-ryaml', '-rjson', '-e', 'puts JSON.generate(YAML.safe_load(STDIN.read))'],
        input=source, text=True, capture_output=True,
    )
    if result.returncode:
        raise ValueError('invalid YAML: ' + result.stderr.splitlines()[0])
    return json.loads(result.stdout)


def metadata_errors(metadata, agent):
    errors = []
    metadata = metadata if isinstance(metadata, dict) else {}
    agent = agent if isinstance(agent, dict) else {}
    if metadata.get('name') != 'index-alpha':
        errors.append('skill name must be index-alpha')
    if not isinstance(metadata.get('description'), str) or not metadata['description'].strip():
        errors.append('skill description is required')
    interface = agent.get('interface', {})
    if not isinstance(interface, dict) or '$index-alpha' not in str(interface.get('default_prompt', '')):
        errors.append('agent default_prompt must name $index-alpha')
    dependencies = agent.get('dependencies', {})
    dependencies = dependencies if isinstance(dependencies, dict) else {}
    tools = dependencies.get('tools', [])
    if not isinstance(tools, list) or not any(
        isinstance(tool, dict) and tool.get('type') == 'mcp' and tool.get('value') == 'index-alpha'
        and tool.get('transport') == 'streamable_http' and tool.get('url') == CANONICAL_ENDPOINT
        for tool in tools
    ):
        errors.append('agent MCP dependency must use canonical streamable HTTP endpoint')
    return errors


def inventory_errors(source: str):
    block = re.search(r'<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->(.*?)<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->', source, re.S)
    if not block:
        return ['missing tool inventory block']
    tools = re.findall(r'^- ([a-z0-9_]+)$', block[1], re.M)
    if not tools or len(tools) != len(set(tools)):
        return ['empty or duplicate tool inventory']
    return []


def guidance_errors(source: str):
    errors = []
    if re.search(r'https?://mcp\.indexalpha\.com(?:/|\b)', source):
        errors.append('retired MCP host guidance')
    if re.search(r'https?://github\.com/index-alpha/(?:skills?|examples)(?:[/#)\s`]|$)', source):
        errors.append('retired repository guidance')
    return errors


def publication_errors(relative: str, source: str):
    errors = []
    parts = Path(relative).parts
    if (any(part in {'.operations', '.state', '.codex', '.omx', 'secrets'} for part in parts)
            or (Path(relative).name.startswith('.env')
                and Path(relative).name not in {'.env.example', '.env.sample'})):
        errors.append('local runtime or secret file must not be published')
    credentials = (r'idx_pat_[A-Za-z0-9]{20,}|(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}'
                   r'|AKIA[0-9A-Z]{16}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----')
    if re.search(credentials, source):
        errors.append('credential-like value or private key must not be published')
    public_templates = {'docs/work/README.md', 'docs/work/active/README.md',
                        'docs/work/inbox/README.md', 'docs/work/archive/README.md'}
    if relative.startswith('docs/work/') and relative not in public_templates:
        errors.append('internal work records must stay outside the public repository')
    private_references = r'/Users/[^/\s]+/|/home/[^/\s]+/|\bapi/mcp/|\bapp/(?:routes|features|components)/|/api/(?:app|ops)/|\binternal/|\bmodules/'
    if Path(relative).suffix in {'.md', '.json', '.yaml', '.yml', '.plist', '.sh'} and re.search(private_references, source):
        errors.append('private checkout, source repository or implementation reference')
    return errors


def markdown_errors(file: Path, root: Path):
    source = file.read_text(encoding='utf-8')
    errors = []
    # Inspect JSON fences separately; ignore all fences and inline code for links.
    for block in re.findall(r'^```json\s*\n(.*?)^```\s*$', source, re.M | re.S):
        try:
            json.loads(block)
        except json.JSONDecodeError as error:
            errors.append(f'invalid JSON example: {error.msg}')
    prose = re.sub(r'^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', source, flags=re.M | re.S)
    prose = re.sub(r'(`+).*?\1', '', prose)
    # Simple inline destinations and reference definitions cover our Markdown.
    destinations = re.findall(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)', prose)
    destinations += re.findall(r'^\s*\[[^\]\n]+\]:\s*(<[^>]+>|\S+)', prose, re.M)
    for destination in destinations:
        destination = destination.strip('<>')
        parsed = urlsplit(destination)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (root if parsed.path.startswith('/') else file.parent) / unquote(parsed.path).lstrip('/')
        if not target.exists():
            errors.append(f'missing local link: {destination}')
    return errors


def validate(root: Path):
    files = subprocess.check_output(['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'], cwd=root).decode().split('\0')
    deleted = set(subprocess.check_output(['git', 'ls-files', '-z', '--deleted'], cwd=root).decode().split('\0'))
    errors = []
    for relative in sorted(set(filter(None, files)) - deleted):
        file = root / relative
        if not file.is_file():
            errors.append(f'{relative}: indexed file missing')
            continue
        errors.extend(f'{relative}: {error}' for error in publication_errors(
            relative, file.read_bytes().decode('utf-8', errors='replace')))
        if file.suffix == '.md':
            errors.extend(f'{relative}: {error}' for error in markdown_errors(file, root))
            errors.extend(f'{relative}: {error}' for error in guidance_errors(file.read_text()))
        elif file.suffix in ('.yaml', '.yml'):
            try:
                read_yaml(file.read_text())
            except (ValueError, UnicodeError) as error:
                errors.append(f'{relative}: {error}')
        elif file.suffix == '.json':
            try:
                json.loads(file.read_text())
            except (ValueError, UnicodeError) as error:
                errors.append(f'{relative}: invalid JSON: {error}')
    skill = root / 'skills/index-alpha'
    try:
        entrypoint = (skill / 'SKILL.md').read_text()
        frontmatter = re.match(r'\A---\n(.*?)\n---(?:\n|$)', entrypoint, re.S)
        if not frontmatter:
            errors.append('SKILL.md: missing frontmatter')
        else:
            errors.extend(metadata_errors(read_yaml(frontmatter[1]), read_yaml((skill / 'agents/openai.yaml').read_text())))
        if len(entrypoint.splitlines()) >= 500:
            errors.append('SKILL.md must stay under 500 lines')
        errors.extend(inventory_errors((skill / 'references/mcp-server-map.md').read_text()))
    except (OSError, ValueError) as error:
        errors.append(str(error))
    return errors


if __name__ == '__main__':
    failures = validate(ROOT)
    if failures:
        print('\n'.join(f'error: {failure}' for failure in failures), file=sys.stderr)
        sys.exit(1)
    print('Repository metadata, JSON examples, skill package and local Markdown links passed.')
