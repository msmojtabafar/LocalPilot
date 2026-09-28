class ConversationContext:
    def __init__(self, max_messages=20):
        self.max_messages = max_messages
        self._messages = []

    def add_message(self, role, content):
        if role not in ("user", "assistant"):
            return False

        self._messages.append({
            "role": role,
            "content": content,
        })

        if len(self._messages) > self.max_messages:
            self._messages = self._messages[-self.max_messages:]

        return True

    def get_messages(self):
        return list(self._messages)

    def clear(self):
        self._messages.clear()

    def __len__(self):
        return len(self._messages)
