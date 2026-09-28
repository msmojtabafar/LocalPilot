from .tool_registry import ToolRegistry


class ToolManager:
    def __init__(self, registry=None):
        self.registry = registry or ToolRegistry()

    def register(self, tool):
        self.registry.register(tool)

    def unregister(self, name):
        if self.registry.get(name) is None:
            return False

        del self.registry._tools[name]
        return True

    def get(self, name):
        return self.registry.get(name)

    def tools(self):
        return self.registry.tools()

    def execute(self, name, args=None, confirmed=False):
        return self.registry.execute(
            name,
            args=args,
            confirmed=confirmed,
        )
