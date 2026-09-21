from localpilot.main import main


def test_main(capsys):
    main()

    captured = capsys.readouterr()

    assert "LocalPilot" in captured.out
    assert "Local AI Assistant" in captured.out
