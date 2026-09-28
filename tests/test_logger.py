from localpilot.logger import Logger


def test_info(capsys):
    logger = Logger()

    logger.info("Information message")

    captured = capsys.readouterr()

    assert captured.out == "[INFO] Information message\n"


def test_warning(capsys):
    logger = Logger()

    logger.warning("Warning message")

    captured = capsys.readouterr()

    assert captured.out == "[WARNING] Warning message\n"


def test_error(capsys):
    logger = Logger()

    logger.error("Error message")

    captured = capsys.readouterr()

    assert captured.out == "[ERROR] Error message\n"


def test_debug(capsys):
    logger = Logger()

    logger.debug("Debug message")

    captured = capsys.readouterr()

    assert captured.out == "[DEBUG] Debug message\n"
