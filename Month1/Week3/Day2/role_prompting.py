from utils import ask
system_prompt = """
You are a senior Python code reviewer.

Review Python code with these rules:
- Be strict.
- Be concise.
- Do not praise the code.
- Give only actionable suggestions.
"""

user_prompt = """
Review this code:

def divide(a, b)
    return a / b

print(divide(10,0))
"""

response = ask(user_prompt, system_prompt)
print(response)