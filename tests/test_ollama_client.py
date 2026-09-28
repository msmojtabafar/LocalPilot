from localpilot.ollama_client import OllamaClient


class DummyResponse:
    def read(self):
        return b'{"response":"Hello from Ollama"}'

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def test_ollama_client():
    client = OllamaClient()

    assert client.model == "llama3.2:3b"


def test_ollama_empty_prompt():
    client = OllamaClient()

    assert client.generate("") is None


def test_ollama_response(monkeypatch):
    def fake_urlopen(*args, **kwargs):
        return DummyResponse()

    monkeypatch.setattr(
        "urllib.request.urlopen",
        fake_urlopen,
    )

    client = OllamaClient()

    result = client.generate("Hello")

    assert result == "Hello from Ollama"
