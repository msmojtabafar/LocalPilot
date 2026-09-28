import json


class AIToolCaller:
    def __init__(self, llm, tool_manager):
        self.llm = llm
        self.tool_manager = tool_manager

    def call(self, prompt, confirmed=False):
        tool_prompt = self._build_prompt(prompt)

        response = self.llm.generate(tool_prompt)

        if not response:
            return None

        request = self._parse_response(response)

        if request is None:
            return response

        if isinstance(request, str):
            return request

        tool_name = request.get("tool")
        args = request.get("args", [])

        if not tool_name:
            return request.get(
                "response",
                response,
            )

        if not isinstance(args, list):
            args = [args]

        result = self.tool_manager.execute(
            tool_name,
            args=args,
            confirmed=confirmed,
        )

        if (
            isinstance(result, dict)
            and result.get("allowed") is False
            and result.get("error") == "Permission denied"
        ):
            result["confirmation_required"] = True
            result["tool"] = tool_name
            result["args"] = args
            result["message"] = (
                "این عملیات نیاز به تأیید شما دارد."
            )

        return result

    def _build_prompt(self, prompt):
        tools = self.tool_manager.tools()

        tool_descriptions = []

        for name in tools:
            tool = self.tool_manager.get(name)

            if tool is None:
                continue

            tool_descriptions.append(
                f"{name}: {tool.description}"
            )

        tools_text = "\n".join(tool_descriptions)

        return f"""
You are LocalPilot.

You MUST follow these rules.

USER LANGUAGE:
The user may speak Persian. Understand Persian requests.

AVAILABLE TOOLS:
{tools_text}

IMPORTANT:
If the user asks for an operation that requires a tool,
you MUST return ONLY JSON.

Do NOT explain anything.
Do NOT write sentences.
Do NOT use markdown.

TOOL JSON FORMAT:
{{"tool":"TOOL_NAME","args":["ARGUMENT1","ARGUMENT2"]}}

NORMAL RESPONSE JSON FORMAT:
{{"response":"YOUR_RESPONSE"}}

EXAMPLES:

User:
لیست فایل های پوشه فعلی را بده

Answer:
{{"tool":"file","args":["list","."]}}

User:
پردازش های در حال اجرا را لیست کن

Answer:
{{"tool":"process","args":["list"]}}

User:
پردازش 1234 را بررسی کن

Answer:
{{"tool":"process","args":["info","1234"]}}

User:
یک دستور برای خاموش کردن کامپیوتر اجرا کن

Answer:
{{"tool":"command","args":["shutdown","-h","now"]}}

User:
سلام

Answer:
{{"response":"سلام"}}

USER REQUEST:
{prompt}
""".strip()

    def _parse_response(self, response):
        try:
            data = json.loads(response)
        except (TypeError, json.JSONDecodeError):
            return None

        if not isinstance(data, dict):
            return None

        if "tool" in data:
            return data

        if "response" in data:
            return data

        return None
