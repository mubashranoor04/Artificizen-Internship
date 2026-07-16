from utils import client


prompt = "Explain deep learning in simple words."


models = [
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile"
]


for model in models:

    print("\nMODEL:", model)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=200
    )


    print("\nResponse:")
    print(response.choices[0].message.content)


    print("\nTotal Tokens:")
    print(response.usage.total_tokens)