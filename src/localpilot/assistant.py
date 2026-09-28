from .ai_tool_caller import AIToolCaller
from .conversation_context import ConversationContext


class LocalPilotAssistant:
    def __init__(self, llm, tool_manager, context=None):
        self.llm = llm
        self.tool_manager = tool_manager
        self.context = context or ConversationContext()

        self.tool_caller = AIToolCaller(
            self.llm,
            self.tool_manager,
        )

    def respond(self, message, confirmed=False):
        if not message or not message.strip():
            return None

        self.context.add_message(
            "user",
            message,
        )

        response = self.tool_caller.call(
            message,
            confirmed=confirmed,
        )

        if response is None:
            response = "I couldn't generate a response."

        self.context.add_message(
            "assistant",
            self._format_for_context(response),
        )

        if isinstance(response, dict):
            if response.get("confirmation_required"):
                return response

            if "allowed" in response:
                if not response["allowed"]:
                    return response.get(
                        "error",
                        "Permission denied",
                    )

                return response.get("result")

        return response

    def _format_for_context(self, response):
        if isinstance(response, dict):
            return str(response)

        return str(response)
