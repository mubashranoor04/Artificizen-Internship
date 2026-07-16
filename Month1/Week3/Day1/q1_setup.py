import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("API key loaded successfully!")
    print("Key starts with:", api_key[:10])
else:
    print("API key not found!")