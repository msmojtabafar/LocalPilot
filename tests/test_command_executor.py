from localpilot.command_executor import CommandExecutor
from localpilot.command_registry import CommandRegistry


def test_execute_registered_command():
    registry = CommandRegistry()

    def handler():
        return "ok"

    registry.register("test", handler)

    executor = CommandExecutor(registry)

    assert executor.execute("test") == "ok"


def test_execute_unknown_command():
    registry = CommandRegistry()

    executor = CommandExecutor(registry)

    assert executor.execute("unknown") is None
