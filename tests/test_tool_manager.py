from localpilot.tool import Tool
from localpilot.tool_manager import ToolManager


class DummyTool(Tool):
    def __init__(self, name="dummy"):
        super().__init__(name, "Dummy tool")

    def execute(self, *args):
        return "executed"


def test_register_and_get():
    manager = ToolManager()
    tool = DummyTool()

    manager.register(tool)

    assert manager.get("dummy") is tool


def test_tools():
    manager = ToolManager()

    manager.register(DummyTool("one"))
    manager.register(DummyTool("two"))

    assert manager.tools() == ["one", "two"]


def test_unregister():
    manager = ToolManager()
    manager.register(DummyTool())

    assert manager.unregister("dummy") is True
    assert manager.get("dummy") is None


def test_unregister_unknown_tool():
    manager = ToolManager()

    assert manager.unregister("unknown") is False


def test_execute_requires_confirmation():
    manager = ToolManager()
    manager.register(DummyTool())

    result = manager.execute("dummy")

    assert result["allowed"] is False
    assert result["error"] == "Permission denied"


def test_execute_with_confirmation():
    manager = ToolManager()
    manager.register(DummyTool())

    result = manager.execute("dummy", confirmed=True)

    assert result["allowed"] is True
    assert result["result"] == "executed"
