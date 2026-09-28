class LLM:
    def generate(self, prompt):
        raise NotImplementedError


class LocalLLM(LLM):
    def __init__(self, client):
        self.client = client

    def generate(self, prompt):
        if not prompt:
            return None

        try:
            return self.client.generate(prompt)
        except Exception:
            return None
