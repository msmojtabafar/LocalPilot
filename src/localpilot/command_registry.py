class CommandRegistry:
    def __init__(self):
        self._commands = {}

    def register(self, name, handler):
        self._commands[name] = handler

    def get(self, name):
        return self._commands.get(name)

    def commands(self):
        return list(self._commands.keys())
