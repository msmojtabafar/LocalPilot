import json
import urllib.request


class OllamaClient:
    def __init__(
        self,
        model="llama3.2:3b",
        host="http://localhost:11434",
    ):
        self.model = model
        self.host = host.rstrip("/")

    def generate(self, prompt):
        if not prompt:
            return None

        payload = json.dumps({
            "model": self.model,
            "prompt": prompt,
            "stream": False,
        }).encode("utf-8")

        request = urllib.request.Request(
            f"{self.host}/api/generate",
            data=payload,
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(
                request,
                timeout=120,
            ) as response:
                data = json.loads(
                    response.read().decode("utf-8")
                )

            return data.get("response")

        except (OSError, ValueError, json.JSONDecodeError):
            return None
