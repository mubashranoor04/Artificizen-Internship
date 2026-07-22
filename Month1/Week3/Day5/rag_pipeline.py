"""
Complete RAG Pipeline for Day 5

Flow:
Load Document
    ↓
Chunk
    ↓
Embed
    ↓
Store in Qdrant
    ↓
Retrieve
    ↓
Prompt
    ↓
Groq
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

from sentence_transformers import SentenceTransformer

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
)

from config import *

load_dotenv()

# Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Embedding Model

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Qdrant

DB_PATH = Path("db")
DB_PATH.mkdir(exist_ok=True)

qdrant = QdrantClient(
    path=str(DB_PATH)
)

# Load Document

def load_document(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()
    
# Chunking

def chunk_text(
    text,
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP,
):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - overlap

    return chunks

# Embeddings

def embed_documents(chunks):

    return embedding_model.encode(chunks)


def embed_query(query):

    return embedding_model.encode(query)

# Database

def create_collection():

    collections = [
        c.name
        for c in qdrant.get_collections().collections
    ]

    if COLLECTION_NAME in collections:

        qdrant.delete_collection(
            COLLECTION_NAME
        )

    qdrant.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE,
        ),
    )


def store_chunks(chunks, source):

    vectors = embed_documents(chunks)

    points = []

    for index, (chunk, vector) in enumerate(
        zip(chunks, vectors),
        start=1,
    ):

        points.append(

            PointStruct(

                id=index,

                vector=vector.tolist(),

                payload={

                    "text": chunk,

                    "source": source,

                    "chunk_index": index,

                },

            )

        )

    qdrant.upsert(

        collection_name=COLLECTION_NAME,

        points=points,

    )

    print(f"Stored {len(points)} chunks.")

# Retrieval

def retrieve(query):

    vector = embed_query(query)

    results = qdrant.query_points(

        collection_name=COLLECTION_NAME,

        query=vector.tolist(),

        limit=TOP_K,

    )

    return results.points


# Prompt

def build_prompt(question, chunks):

    context = ""

    for index, chunk in enumerate(chunks, start=1):

        context += f"\nContext {index}\n"

        context += chunk.payload["text"]

        context += "\n"

    prompt = f"""

You are a helpful AI assistant.

Use ONLY the context below.

If the answer is not present,
reply exactly:

I don't know.

{context}

Question:

{question}

Answer:

"""

    return prompt

# Build Database

def initialize_database():

    document = load_document(
        "data/sample.txt"
    )

    chunks = chunk_text(document)

    create_collection()

    store_chunks(
        chunks,
        "sample.txt",
    )

# Main RAG

def answer_question(

    question,

    history=None,

):

    retrieved_chunks = retrieve(
        question
    )

    prompt = build_prompt(
        question,
        retrieved_chunks,
    )

    messages = []

    if history:

        messages.extend(history)

    messages.append(

        {

            "role": "user",

            "content": prompt,

        }

    )

    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=messages,

        temperature=0,

    )

    answer = response.choices[0].message.content.strip()

    sources = []

    for chunk in retrieved_chunks:

        sources.append(

            {

                "source": chunk.payload["source"],

                "chunk_index": chunk.payload["chunk_index"],

            }

        )

    return {

        "answer": answer,

        "sources": sources,

    }

# Streaming

def stream_answer(

    question,

    history=None,

):

    retrieved_chunks = retrieve(
        question
    )

    prompt = build_prompt(
        question,
        retrieved_chunks,
    )

    messages = []

    if history:

        messages.extend(history)

    messages.append(

        {

            "role": "user",

            "content": prompt,

        }

    )

    stream = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=messages,

        stream=True,

        temperature=0,

    )

    for chunk in stream:

        delta = chunk.choices[0].delta.content

        if delta:

            yield delta