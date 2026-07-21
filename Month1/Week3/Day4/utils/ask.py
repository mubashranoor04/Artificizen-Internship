import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=api_key)


def ask(
    prompt,
    system=None,
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    max_tokens=512,
):
    """
    Send a prompt to Groq and return only the generated text.
    """

    messages = []

    if system:
        messages.append(
            {
                "role": "system",
                "content": system,
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    answer = ask("What is Retrieval-Augmented Generation?")
    print(answer)