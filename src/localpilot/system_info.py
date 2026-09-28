import os
import platform
import socket
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

    def get_local_ip(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.connect(("8.8.8.8", 80))
                return sock.getsockname()[0]
        except OSError:
            return None

    def get_network_interfaces(self):
        try:
            return socket.if_nameindex()
        except OSError:
            return []
