from utils import ask


system_message = """
You are a strict JSON-only responder.
Never output anything outside a JSON object.
"""


response = ask(
    "Give me information about Python programming.",
    system=system_message
)


print(response)