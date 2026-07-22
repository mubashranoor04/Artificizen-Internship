"""
Day 5 - FastAPI RAG Application
"""

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from rag_pipeline import (
    initialize_database,
    answer_question,
    stream_answer,
)

from cache import (
    get_cached_answer,
    save_to_cache,
)

from memory import (
    get_history,
    update_history,
)

app = FastAPI(
    title="Day 5 RAG API",
    version="1.0",
)


# --------------------------
# Build database once
# --------------------------

@app.on_event("startup")
def startup():

    print("Initializing database...")

    initialize_database()

    print("Database ready.")


# --------------------------
# Request Model
# --------------------------

class ChatRequest(BaseModel):

    session_id: str

    query: str


# --------------------------
# POST /chat
# --------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    # ----------------------
    # Check Cache
    # ----------------------

    cached = get_cached_answer(request.query)

    if cached:

        return cached

    # ----------------------
    # Conversation History
    # ----------------------

    history = get_history(
        request.session_id
    )

    # ----------------------
    # RAG
    # ----------------------

    result = answer_question(

        question=request.query,

        history=history,

    )

    # ----------------------
    # Update Memory
    # ----------------------

    update_history(

        request.session_id,

        request.query,

        result["answer"],

    )

    # ----------------------
    # Save Cache
    # ----------------------

    save_to_cache(

        request.query,

        result["answer"],

        result["sources"],

    )

    return result


# --------------------------
# Streaming Endpoint
# --------------------------

@app.post("/stream")
def stream(request: ChatRequest):

    history = get_history(
        request.session_id
    )

    generator = stream_answer(

        question=request.query,

        history=history,

    )

    return StreamingResponse(

        generator,

        media_type="text/plain",

    )


# --------------------------
# Root
# --------------------------

@app.get("/")
def root():

    return {

        "message": "Day 5 RAG API Running"

    }