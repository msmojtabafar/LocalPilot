from .permission_manager import PermissionManager


class ToolRegistry:
    def __init__(self, permission_manager=None):
        self._tools = {}
        self.permission_manager = permission_manager or PermissionManager()

    def register(self, tool):
        self._tools[tool.name] = tool

    def get(self, name):
        return self._tools.get(name)

    def tools(self):
        return list(self._tools.keys())

    def execute(self, name, args=None, confirmed=False):
        tool = self.get(name)

        if tool is None:
            return None

        if args is None:
            args = []

        if not self.permission_manager.is_allowed(
            name,
            confirmed=confirmed,
        ):
            return {
                "allowed": False,
                "error": "Permission denied",
            }

        result = tool.execute(*args)

        return {
            "allowed": True,
            "result": result,
        }
