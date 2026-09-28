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
                if not entry.isdigit():
                    continue

                pid = int(entry)

                try:
                    name = self._get_process_name(pid)

                    processes.append({
                        "pid": pid,
                        "name": name,
                    })

                except (
                    FileNotFoundError,
                    PermissionError,
                    OSError,
                ):
                    continue

        except OSError:
            return []

        return sorted(
            processes,
            key=lambda process: process["pid"],
        )

    def _get_process_info(self, pid):
        if pid is None:
            return None

        try:
            pid = int(pid)

            if pid <= 0:
                return None

            name = self._get_process_name(pid)

            return {
                "pid": pid,
                "name": name,
            }

        except (
            ValueError,
            FileNotFoundError,
            PermissionError,
            OSError,
        ):
            return None

    def _get_process_name(self, pid):
        with open(
            f"/proc/{pid}/comm",
            "r",
            encoding="utf-8",
        ) as file:
            return file.read().strip()
