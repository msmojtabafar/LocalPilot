from localpilot.llm import LLM, LocalLLM


class DummyClient:
    def generate(self, prompt):
        return f"Response: {prompt}"


class FailingClient:
    def generate(self, prompt):
        raise RuntimeError("Connection failed")


def test_llm_is_abstract_interface():
    llm = LLM()

    try:
        llm.generate("hello")
        assert False
    except NotImplementedError:
        assert True


def test_local_llm_generate():
    llm = LocalLLM(DummyClient())

    result = llm.generate("hello")

    assert result == "Response: hello"


def test_empty_prompt():
    llm = LocalLLM(DummyClient())

    assert llm.generate("") is None


def test_llm_error():
    llm = LocalLLM(FailingClient())

    assert llm.generate("hello") is None
