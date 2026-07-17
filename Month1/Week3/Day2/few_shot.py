from utils import ask
messages = [
    "My order arrived but it was missing one piece.",
    "What are your salon timings?",
    "I took wash and blow dry from your salon and loved it.",
    "I got rotten apples in my parcel.",
    "Do you have imports of Chanel bags?"
]
for message in messages:
    prompt = f"""
Classify the following customer message into exactly one of these categories:

- Complaint
- Question
- Compliment

Here are some examples:

Example 1
Message: "My package arrived damaged."
Category: Complaint

Example 2
Message: "What time does your store open?"
Category: Question

Example 3
Message: "Your customer service was excellent!"
Category: Compliment

Now classify the following customer message.

Customer message:
"{message}"

Return only the category name.
"""

    response = ask(prompt)

    print(f"Message: {message}")
    print(f"Classification: {response}")
    print("-" * 50)