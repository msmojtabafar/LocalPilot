import os

from .tool import Tool


class ProcessTool(Tool):
    def __init__(self):
        super().__init__(
            "process",
            "List running processes and get process information",
        )

    def execute(self, action, pid=None):
        if action == "list":
            return self._list_processes()

        if action == "info":
            return self._get_process_info(pid)

        return None

    def _list_processes(self):
        processes = []

        try:
            for entry in os.listdir("/proc"):
                if entry.isdigit():
                    processes.append(int(entry))
        except OSError:
            return []

        return sorted(processes)

    def _get_process_info(self, pid):
        if pid is None:
            return None

        try:
            pid = int(pid)

            if pid <= 0:
                return None

            with open(f"/proc/{pid}/comm", "r", encoding="utf-8") as file:
                name = file.read().strip()

            return {
                "pid": pid,
                "name": name,
            }

        except (ValueError, FileNotFoundError, PermissionError, OSError):
            return None
