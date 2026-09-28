import json


class AIToolCaller:
    def __init__(self, llm, tool_manager):
        self.llm = llm
        self.tool_manager = tool_manager

    def call(self, prompt, confirmed=False):
        response = self.llm.generate(prompt)

        if not response:
            return None

        request = self._parse_response(response)

        if request is None:
            return response

        tool_name = request.get("tool")
        args = request.get("args", [])

        if not tool_name:
            return response

        if not isinstance(args, list):
            args = [args]

        return self.tool_manager.execute(
            tool_name,
            args=args,
            confirmed=confirmed,
        )

    def _parse_response(self, response):
        try:
            data = json.loads(response)
        except (TypeError, json.JSONDecodeError):
            return None

        if not isinstance(data, dict):
            return None

        if "tool" not in data:
            return None

        return data
