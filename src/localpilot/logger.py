class Logger:
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

    def info(self, message):
        self._log(self.INFO, message)

    def warning(self, message):
        self._log(self.WARNING, message)

    def error(self, message):
        self._log(self.ERROR, message)

    def debug(self, message):
        self._log(self.DEBUG, message)

    def _log(self, level, message):
        print(f"[{level}] {message}")
