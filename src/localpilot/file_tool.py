from pathlib import Path

from .tool import Tool


class FileTool(Tool):
    def __init__(self):
        super().__init__(
            "file",
            "Read, write, list, and create files and directories",
        )

    def execute(self, action, path, content=None):
        target = Path(path)

        try:
            if action == "read":
                return target.read_text(encoding="utf-8")

            if action == "write":
                target.write_text(content or "", encoding="utf-8")
                return True

            if action == "list":
                return [item.name for item in target.iterdir()]

            if action == "mkdir":
                target.mkdir(parents=True, exist_ok=True)
                return True

            return None

        except (OSError, UnicodeError):
            return None
