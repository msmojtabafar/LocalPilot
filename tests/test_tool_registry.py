from localpilot.tool import Tool
from localpilot.tool_registry import ToolRegistry


class DummyTool(Tool):
    def execute(self):
        return "executed"


def test_register_tool():
    registry = ToolRegistry()
    tool = DummyTool("test", "Test tool")

    registry.register(tool)

    assert registry.get("test") is tool


def test_unknown_tool():
    registry = ToolRegistry()

    assert registry.get("unknown") is None


def test_tools():
    registry = ToolRegistry()
    tool = DummyTool("test", "Test tool")

    registry.register(tool)

    assert "test" in registry.tools()
