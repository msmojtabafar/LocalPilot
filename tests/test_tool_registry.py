from localpilot.tool import Tool
from localpilot.tool_registry import ToolRegistry
from localpilot.permission_manager import PermissionManager


class DummyTool(Tool):
    def __init__(self, name="dummy"):
        super().__init__(name, "Dummy tool")

    def execute(self, *args):
        return "executed"


def test_register_tool():
    registry = ToolRegistry()

    tool = DummyTool()
    registry.register(tool)

    assert registry.get("dummy") is tool


def test_tools():
    registry = ToolRegistry()

    registry.register(DummyTool("one"))
    registry.register(DummyTool("two"))

    assert registry.tools() == ["one", "two"]


def test_safe_tool_execution():
    manager = PermissionManager()
    manager.set_permission("dummy", PermissionManager.SAFE)

    registry = ToolRegistry(manager)
    registry.register(DummyTool())

    result = registry.execute("dummy")

    assert result["allowed"] is True
    assert result["result"] == "executed"


def test_dangerous_tool_requires_confirmation():
    registry = ToolRegistry()
    registry.register(DummyTool())

    result = registry.execute("dummy")

    assert result["allowed"] is False
    assert result["error"] == "Permission denied"


def test_dangerous_tool_with_confirmation():
    registry = ToolRegistry()
    registry.register(DummyTool())

    result = registry.execute("dummy", confirmed=True)

    assert result["allowed"] is True
    assert result["result"] == "executed"


def test_unknown_tool():
    registry = ToolRegistry()

    assert registry.execute("unknown") is None
