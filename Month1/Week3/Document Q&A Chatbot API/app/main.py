from fastapi import FastAPI

from api.routes import router

app = FastAPI(
    title="Document Q&A Chatbot API"
)
app.include_router(router)

@app.get("/")
def home():

    return {
        "message":
        "Document Q&A Chatbot API running"
    }