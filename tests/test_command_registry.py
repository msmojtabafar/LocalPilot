from localpilot.command_registry import CommandRegistry


def test_register_command():
    registry = CommandRegistry()

    def handler():
        return "ok"

    registry.register("test", handler)

    assert registry.get("test") is handler


def test_get_unknown_command():
    registry = CommandRegistry()

    assert registry.get("unknown") is None


def test_list_commands():
    registry = CommandRegistry()

    registry.register("help", lambda: None)
    registry.register("status", lambda: None)
    registry.register("exit", lambda: None)

    assert registry.commands() == ["help", "status", "exit"]
