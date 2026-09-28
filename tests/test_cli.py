from localpilot.cli import CLI


def test_help(capsys):
    cli = CLI()

    cli.handle_command("help")

    captured = capsys.readouterr()

    assert "Available commands:" in captured.out
    assert "help" in captured.out
    assert "status" in captured.out
    assert "exit" in captured.out


def test_status(capsys):
    cli = CLI()

    cli.handle_command("status")

    captured = capsys.readouterr()

    assert "LocalPilot is running." in captured.out


def test_exit(capsys):
    cli = CLI()

    cli.handle_command("exit")

    captured = capsys.readouterr()

    assert cli.running is False
    assert "Goodbye!" in captured.out


def test_unknown_command(capsys):
    cli = CLI()

    cli.handle_command("something")

    captured = capsys.readouterr()

    assert "Unknown command: something" in captured.out


def test_cli_uses_registry():
    cli = CLI()

    assert "help" in cli.registry.commands()
    assert "status" in cli.registry.commands()
    assert "exit" in cli.registry.commands()


def test_cli_uses_executor():
    cli = CLI()

    assert cli.executor.registry is cli.registry


def test_echo_arguments(capsys):
    cli = CLI()

    cli.handle_command("echo hello world")

    captured = capsys.readouterr()

    assert "hello world" in captured.out
