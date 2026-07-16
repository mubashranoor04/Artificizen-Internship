import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


prompt = "Suggest a creative name for a coffee shop."


print("Temperature 0")

for i in range(3):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"\nResponse {i+1}:")
    print(response.choices[0].message.content)



print("\nTemperature 1")

for i in range(3):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=1.0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(f"\nResponse {i+1}:")
    print(response.choices[0].message.content)