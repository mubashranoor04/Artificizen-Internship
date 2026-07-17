from utils import ask

meeting = """
Team Meeting

Sarah will prepare the presentation by Friday.

Ali needs to fix the login bug today.

Emma should schedule a client meeting next week.

John will update the project documentation.
"""

# Step 1: Extract Action Items

prompt1 = f"""
Extract only the action items from the following meeting transcript.

Meeting Transcript:
{meeting}

Return only a numbered list of action items.
"""

actions = ask(prompt1)

print("Step 1 Output")
print(actions)

print("=" * 50)

# Step 2: Assign Priorities

prompt2 = f"""
Assign a priority (High, Medium, or Low) to each action item.

Action Items:
{actions}

Return ONLY a numbered list in this exact format:

1. Sarah - Prepare the presentation by Friday - High
2. Ali - Fix the login bug today - High
3. Emma - Schedule a client meeting next week - Medium
4. John - Update the project documentation - Low

Do not explain your choices.
Do not add extra text.
"""

priorities = ask(prompt2)

print("Step 2 Output")
print(priorities)

print("=" * 50)

# Step 3: Convert to JSON

prompt3 = f"""
Convert the following action items into a JSON array.

Action Items:
{priorities}

Each object must contain exactly these keys:

{{
  "name": "",
  "task": "",
  "priority": ""
}}

Return ONLY valid JSON.

Do not include markdown.
Do not explain anything.
"""

json_output = ask(prompt3)

print("Step 3 Output")
print(json_output)