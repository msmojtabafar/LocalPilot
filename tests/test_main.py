from localpilot.main import main


def test_main(monkeypatch, capsys):
    commands = iter(["exit"])

    monkeypatch.setattr("builtins.input", lambda _: next(commands))

    main()

    captured = capsys.readouterr()

    assert "LocalPilot" in captured.out
    assert "Local AI Assistant" in captured.out
    assert "Goodbye!" in captured.out
