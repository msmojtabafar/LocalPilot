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
    assert "Type 'help' for available commands." in captured.out
