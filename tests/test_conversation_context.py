from localpilot.conversation_context import ConversationContext


def test_context_starts_empty():
    context = ConversationContext()

    assert context.get_messages() == []
    assert len(context) == 0


def test_add_user_message():
    context = ConversationContext()

    assert context.add_message("user", "Hello") is True

    assert context.get_messages() == [
        {
            "role": "user",
            "content": "Hello",
        }
    ]


def test_add_assistant_message():
    context = ConversationContext()

    context.add_message("assistant", "Hello!")

    assert context.get_messages()[0]["role"] == "assistant"


def test_invalid_role():
    context = ConversationContext()

    assert context.add_message("system", "Hello") is False
    assert len(context) == 0


def test_multiple_messages():
    context = ConversationContext()

    context.add_message("user", "Hello")
    context.add_message("assistant", "Hi")
    context.add_message("user", "How are you?")

    assert len(context) == 3


def test_max_messages():
    context = ConversationContext(max_messages=2)

    context.add_message("user", "one")
    context.add_message("assistant", "two")
    context.add_message("user", "three")

    assert context.get_messages() == [
        {
            "role": "assistant",
            "content": "two",
        },
        {
            "role": "user",
            "content": "three",
        },
    ]


def test_clear():
    context = ConversationContext()

    context.add_message("user", "Hello")
    context.add_message("assistant", "Hi")

    context.clear()

    assert context.get_messages() == []
    assert len(context) == 0


def test_get_messages_returns_copy():
    context = ConversationContext()

    context.add_message("user", "Hello")

    messages = context.get_messages()
    messages.clear()

    assert len(context) == 1
