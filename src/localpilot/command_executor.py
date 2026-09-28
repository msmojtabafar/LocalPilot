class CommandExecutor:
    def __init__(self, registry):
        self.registry = registry

    def execute(self, name, args=None):
        handler = self.registry.get(name)

        if handler is None:
            return None

        if args is None:
            args = []

        return handler(*args)
