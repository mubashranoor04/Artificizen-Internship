from utils import ask
logic_puzzle = """
Sarah is taller than John.
John is taller than Emma.

Who is the tallest?
"""

# Without Chain-of-Thought
prompt1 = f"""
Answer the following logic puzzle.

{logic_puzzle}
"""

response1 = ask(prompt1)

print("Without Chain-of-Thought:")
print(response1)

print("-" * 50)

# With Chain-of-Thought
prompt2 = f"""
Answer the following logic puzzle.

{logic_puzzle}

Think step by step before answering.
"""

response2 = ask(prompt2)

print("With Chain-of-Thought:")
print(response2)