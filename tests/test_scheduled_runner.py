"""Exercise process/log boundaries without model calls or credentials."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

RUNNER = Path(__file__).resolve().parents[1] / 'examples/scheduling/run.sh'


class ScheduledRunnerTests(unittest.TestCase):
    def run_fake(self, exit_code=0, locked=False, extra_args=()):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prompt = root / 'prompt.md'
            prompt.write_text('Run the workflows.\n')
            fake = root / 'codex'
            fake.write_text('#!/bin/bash\nprintf "%s\\n" "$@" > "$ARG_CAPTURE"\ncat > "$CAPTURE"\nprintf \'{"raw":"upload-ticket"}\\n\'\nprintf "diagnostic\\n" >&2\nexit ' + str(exit_code) + '\n')
            fake.chmod(0o755)
            logs = root / 'logs'
            logs.mkdir()
            if locked:
                (logs / '.lock').mkdir()
            env = {**os.environ, 'CODEX_BIN': str(fake), 'RUN_LOG_ROOT': str(logs), 'CAPTURE': str(root / 'input'), 'ARG_CAPTURE': str(root / 'args')}
            result = subprocess.run(['bash', str(RUNNER), str(prompt), *extra_args], env=env, capture_output=True, text=True)
            runs = [p for p in logs.iterdir() if p.is_dir() and p.name != '.lock']
            if locked:
                self.assertEqual(result.returncode, 0)
                self.assertEqual(runs, [])
                self.assertFalse((root / 'input').exists())
                return
            self.assertEqual(result.returncode, exit_code, result.stderr)
            self.assertEqual(len(runs), 1)
            self.assertEqual((runs[0] / 'events.jsonl').read_text(), '{"raw":"upload-ticket"}\n')
            self.assertEqual((runs[0] / 'stderr.log').read_text(), 'diagnostic\n')
            self.assertEqual((runs[0] / 'exit-code').read_text().strip(), str(exit_code))
            self.assertIn('Run the workflows.', (root / 'input').read_text())
            self.assertFalse((logs / '.lock').exists())
            args = (root / 'args').read_text().splitlines()
            for arg in extra_args:
                self.assertIn(arg, args)

    def test_raw_logs_are_preserved(self):
        self.run_fake()

    def test_failure_status_and_logs_survive(self):
        self.run_fake(exit_code=7)

    def test_overlapping_launch_skips(self):
        self.run_fake(locked=True)

    def test_forwards_run_specific_mcp_configuration(self):
        self.run_fake(extra_args=('-c', 'mcp_servers.example.bearer_token_env_var="EXAMPLE_TOKEN"'))

    def test_lock_creation_error_is_not_a_successful_skip(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            prompt = root / 'prompt.md'
            prompt.write_text('Read only.\n')
            (root / '.lock').write_text('Not a lock directory')
            result = subprocess.run(['bash', str(RUNNER), str(prompt)],
                                    env={**os.environ, 'RUN_LOG_ROOT': str(root)},
                                    capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertNotIn('Another run holds', result.stdout)
