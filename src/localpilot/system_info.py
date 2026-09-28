import os
import platform
import socket
import sys
import shutil


class SystemInfo:
    def get_os(self):
        return platform.system()

    def get_python_version(self):
        return platform.python_version()

    def get_hostname(self):
        return socket.gethostname()

    def get_cpu_count(self):
        return os.cpu_count()

    def get_memory(self):
        try:
            with open("/proc/meminfo", "r", encoding="utf-8") as file:
                for line in file:
                    if line.startswith("MemTotal:"):
                        return int(line.split()[1]) * 1024
        except (FileNotFoundError, ValueError):
            return None

        return None

    def get_disk(self):
        try:
            total, used, free = shutil.disk_usage("/")
            return {
                "total": total,
                "used": used,
                "free": free,
            }
        except OSError:
            return None
