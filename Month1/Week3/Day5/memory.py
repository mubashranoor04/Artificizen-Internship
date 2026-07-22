"""
Conversation memory.
Stores the last six turns for every session.
"""

from collections import defaultdict

from config import MEMORY_LIMIT

conversation_memory = defaultdict(list)


def get_history(session_id):

    return conversation_memory[session_id]


def update_history(session_id, user_message, assistant_message):

    history = conversation_memory[session_id]

    history.append(
        {
            "role": "user",
            "content": user_message,
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )

    if len(history) > MEMORY_LIMIT * 2:
        conversation_memory[session_id] = history[-MEMORY_LIMIT * 2:]