import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask(
    prompt,
    system=None,
    model="llama-3.1-8b-instant",
    temperature=0.7,
    max_tokens=512
):

    messages = []

    if system:
        messages.append(
            {
                "role": "system",
                "content": system
            }
        )

    messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content