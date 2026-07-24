from fastapi.responses import StreamingResponse

from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File

from models.schemas import (
    ChatRequest,
    ChatResponse
)

from rag.pipeline import ask, stream_answer
from rag.ingest import ingest_document


router = APIRouter()


@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):

    upload_path = Path("documents") / file.filename

    with open(upload_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = ingest_document(str(upload_path))

    return {
        "message": "Document ingested successfully",
        "chunks": chunks
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    answer, sources = ask(
    request.session_id,
    request.query
)

    return ChatResponse(
        answer=answer,
        sources=sources
    )
@router.post("/chat/stream")
def chat_stream(request: ChatRequest):

    return StreamingResponse(

        stream_answer(
            request.session_id,
            request.query
        ),

        media_type="text/plain"
    )