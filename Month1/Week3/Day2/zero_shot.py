from utils import ask
messages = [
    "My order arrived but it was missing one piece. ",
    "What are your salon timings?",
    "I took wash and blow dry from your salon and loved it. ",
    "I got rotten apples in my parcel. ",
    "Do you have imports of Chanel bags? "
]

for message in messages:
    prompt = f"""
Classify the following customer message into exactly one of these categories:

- Complaint
- Question
- Compliment

Return only the category name.

Customer message:
"{message}"
"""

    response = ask(prompt)

    print(f"Message: {message}")
    print(f"Classification: {response}")
    print("-" * 40)