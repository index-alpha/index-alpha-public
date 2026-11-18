"""Failure cases for the portable repository checks."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

SPEC = importlib.util.spec_from_file_location("repository_check", Path(__file__).parents[1] / "scripts/check_repository.py")
check = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check)


class RepositoryChecksTest(unittest.TestCase):
    def check_workflow_contract(self, example, *, checkout_under_work=False):
        """Exercise the Ruby contract lane without a backend or generated plan."""
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            if checkout_under_work:
                root = root / 'work' / 'repository'
                root.mkdir(parents=True)
            skill = root / 'skill'
            (skill / 'references').mkdir(parents=True)
            examples = root / 'examples'
            examples.mkdir()
            schema = {'update_index': {'input': {
                'required': ['acting_agent_id', 'index_id'],
                'additionalProperties': False,
                'properties': {'acting_agent_id': {}, 'index_id': {}},
            }}}
            (root / 'schemas.json').write_text(json.dumps(schema))
            valid = {'tool': 'update_index', 'arguments': {'acting_agent_id': 'actor', 'index_id': 'index'}}
            (skill / 'SKILL.md').write_text(
                '```json\n' + json.dumps(valid) + '\n```\n')
            (skill / 'references/mcp-server-map.md').write_text(
                '<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->\n- update_index\n'
                '<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->\n')
            (examples / 'setup.md').write_text('```json\n' + json.dumps(example) + '\n```\n')
            checker = Path(__file__).parents[1] / 'scripts/check_mcp_shapes.rb'
            return subprocess.run(
                ['ruby', '-rjson', str(checker), str(root / 'schemas.json'), str(skill), str(examples)],
                text=True, capture_output=True,
            )

    def test_workflow_contract_needs_no_generated_plan(self):
        result = self.check_workflow_contract({
            'tool': 'update_index', 'arguments': {'acting_agent_id': 'actor', 'index_id': 'index'},
        })
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('2 documented example argument shapes checked', result.stdout)

    def test_workflow_contract_in_work_named_checkout(self):
        result = self.check_workflow_contract({
            'tool': 'update_index', 'arguments': {'acting_agent_id': 'actor', 'index_id': 'index'},
        }, checkout_under_work=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('2 documented example argument shapes checked', result.stdout)

    def test_workflow_contract_rejects_unknown_tool(self):
        result = self.check_workflow_contract({'tool': 'invented_tool', 'arguments': {}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('unknown example tool invented_tool', result.stderr)

    def test_workflow_contract_rejects_missing_required_argument(self):
        result = self.check_workflow_contract({'tool': 'update_index', 'arguments': {'index_id': 'index'}})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('missing fields ["acting_agent_id"]', result.stderr)

    def test_public_documents_reject_private_implementation_references(self):
        for source in (
            '/Users/alice/dev/private-project',
            'app/routes/private-screen.tsx',
            'api/mcp/example_handler.go',
            '/api/app/v1/private',
            '/api/ops/v1/private',
        ):
            self.assertTrue(check.publication_errors('docs/guide.md', source), source)
        self.assertEqual(check.publication_errors(
            'docs/reference/mcp.md', 'https://api.indexalpha.com/mcp list_agents platform://mcp/usage-guide'), [])

    def test_work_records_are_private_but_workflow_templates_are_public(self):
        self.assertTrue(check.publication_errors('docs/work/active/private-plan/design.md', 'Plan'))
        self.assertTrue(check.publication_errors('docs/work/active/private-plan/README.md', 'Plan'))
        self.assertTrue(check.publication_errors('docs/work/active/private-plan/data.json', '{}'))
        self.assertEqual(check.publication_errors('docs/work/active/README.md', 'Workflow'), [])

    def test_publication_rejects_credentials_in_any_text_file(self):
        for path in ('docs/guide.md', 'example.json', 'client.yaml', 'run.sh'):
            for secret in ('idx_' + 'pat_' + 'A' * 40,
                           'gh' + 'p_' + 'b' * 36,
                           '-----BEGIN ' + 'PRIVATE KEY-----'):
                self.assertTrue(check.publication_errors(path, secret), path)
        self.assertEqual(check.publication_errors('example.json', '{"token_env": "INDEX_ALPHA_TOKEN"}'), [])

    def test_publication_rejects_forced_local_runtime_and_secret_paths(self):
        for path in ('.env', 'client/.env.production', 'examples/.operations/bindings.json',
                     'examples/.state/run.json', '.codex/config.toml', '.omx/state.json', 'secrets/token.txt'):
            self.assertTrue(check.publication_errors(path, ''), path)
        self.assertEqual(check.publication_errors('.env.example', 'TOKEN=replace-me'), [])

    def test_deleted_tracked_document_does_not_fail_worktree_validation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            obsolete = root / 'obsolete.md'
            obsolete.write_text('Old example\n')
            subprocess.run(['git', 'add', 'obsolete.md'], cwd=root, check=True)
            obsolete.unlink()
            skill = root / 'skills/index-alpha'
            (skill / 'references').mkdir(parents=True)
            (skill / 'agents').mkdir()
            (skill / 'SKILL.md').write_text('---\nname: index-alpha\ndescription: Test skill\n---\n')
            (skill / 'agents/openai.yaml').write_text(
                'interface:\n  default_prompt: Use $index-alpha\n'
                'dependencies:\n  tools:\n    - type: mcp\n      value: index-alpha\n'
                '      transport: streamable_http\n      url: https://api.indexalpha.com/mcp\n')
            (skill / 'references/mcp-server-map.md').write_text(
                '<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->\n- list_agents\n'
                '<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->\n')
            self.assertEqual(check.validate(root), [])

    def test_missing_link_fails_but_code_and_external_links_are_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "README.md"
            page.write_text('`[code](missing.md)`\n```md\n[fenced](missing.md)\n```\n[web](https://example.com)\n[fragment](#hello)\n')
            self.assertEqual(check.markdown_errors(page, root), [])
            page.write_text('[missing](missing.md)\n')
            self.assertIn('missing local link', check.markdown_errors(page, root)[0])

    def test_missing_reference_link_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "README.md"
            page.write_text('[guide][guide]\n\n[guide]: missing.md\n')
            self.assertIn('missing local link', check.markdown_errors(page, root)[0])

    def test_malformed_json_example_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            page = root / "README.md"
            page.write_text('```json\n{"tool": broken}\n```\n')
            self.assertIn('invalid JSON', check.markdown_errors(page, root)[0])

    def test_malformed_yaml_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "metadata.yaml"
            file.write_text('interface: [broken\n')
            with self.assertRaises(ValueError):
                check.read_yaml(file.read_text())

    def test_retired_host_and_repo_fail(self):
        for value in ('https://mcp.indexalpha.com/mcp', 'https://github.com/index-alpha/skill', 'https://github.com/index-alpha/skills'):
            self.assertTrue(check.guidance_errors(value), value)
        self.assertEqual(check.guidance_errors('https://api.indexalpha.com/mcp https://github.com/index-alpha/index-alpha-public'), [])

    def test_duplicate_tool_inventory_fails(self):
        self.assertTrue(check.inventory_errors('<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_START -->\n- list_agents\n- list_agents\n<!-- INDEX_ALPHA_MCP_TOOL_INVENTORY_END -->'))

    def test_wrong_metadata_and_dependency_fail(self):
        errors = check.metadata_errors({'name': 'wrong', 'description': ''}, {'interface': {'default_prompt': 'missing'}, 'dependencies': {'tools': []}})
        self.assertEqual(len(errors), 4)


if __name__ == '__main__':
    unittest.main()
