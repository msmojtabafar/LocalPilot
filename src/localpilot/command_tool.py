import subprocess

from .tool import Tool


class CommandTool(Tool):
    def __init__(self):
        super().__init__(
            "command",
            "Execute a system command"
        )

    def execute(self, *args):
        if not args:
            return {
                "returncode": 1,
                "stdout": "",
                "stderr": "No command provided",
            }

        try:
            result = subprocess.run(
                list(args),
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )

            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

        except (OSError, subprocess.TimeoutExpired) as error:
            return {
                "returncode": 1,
                "stdout": "",
                "stderr": str(error),
            }
