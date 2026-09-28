import pytest

from localpilot.tool import Tool


class DummyTool(Tool):
    def execute(self, *args, **kwargs):
        return "executed"


def test_tool_properties():
    tool = DummyTool("test", "Test tool")

    assert tool.name == "test"
    assert tool.description == "Test tool"


def test_tool_execute():
    tool = DummyTool("test", "Test tool")

    assert tool.execute() == "executed"


def test_base_tool_execute():
    tool = Tool("test", "Test tool")

    with pytest.raises(NotImplementedError):
        tool.execute()
