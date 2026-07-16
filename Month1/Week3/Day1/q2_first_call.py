import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

# Send request to the model
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    messages=[
        {
            "role": "user",
            "content": "Summarise what a transformer model does in 3 sentences."
        }
    ]
)

# Print only the AI's response
print(response.choices[0].message.content)
print("\n--- Token Usage ---")
print(response.usage)