class CommandExecutor:
    def __init__(self, registry):
        self.registry = registry

    def execute(self, name):
        handler = self.registry.get(name)

        if handler is None:
            return None

        return handler()
