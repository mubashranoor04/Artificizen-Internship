import os

from dotenv import load_dotenv


load_dotenv()



class Settings:


    PROJECT_NAME = "Document Q&A Chatbot API"


    GROQ_API_KEY = os.getenv(
        "GROQ_API_KEY"
    )


    GROQ_MODEL = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile"
    )


    EMBEDDING_MODEL = (
        "all-MiniLM-L6-v2"
    )


    DOCUMENT_FOLDER = "documents"


    VECTORSTORE_PATH = "vectorstore"



settings = Settings()