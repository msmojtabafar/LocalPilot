import platform
import socket
import sys


class SystemInfo:
    def get_os(self):
        return platform.system()

    def get_python_version(self):
        return platform.python_version()

    def get_hostname(self):
        return socket.gethostname()
