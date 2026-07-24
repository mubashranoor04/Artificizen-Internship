# Document Q&A Chatbot API

A production-style **Retrieval Augmented Generation (RAG) based Document Question Answering API** built with **FastAPI**, **Qdrant Vector Database**, **Sentence Transformers**, and **Groq LLM inference**.

The system allows users to upload documents, convert their content into embeddings, store them in a vector database, and ask natural language questions. The chatbot retrieves relevant document sections and generates grounded answers using an LLM.

---

# Features

## Document Processing

- Upload and ingest text documents
- Automatic text splitting into smaller chunks
- Generate semantic embeddings using Sentence Transformers
- Store embeddings with metadata in Qdrant

## RAG Pipeline

Complete Retrieval Augmented Generation workflow:

```
Document
   |
   ↓
Text Extraction
   |
   ↓
Chunking
   |
   ↓
Embedding Generation
   |
   ↓
Vector Storage (Qdrant)
   |
   ↓
User Query
   |
   ↓
Query Embedding
   |
   ↓
Semantic Search
   |
   ↓
Context Retrieval
   |
   ↓
LLM Generation
   |
   ↓
Final Answer
```

---

# Tech Stack

## Backend

- FastAPI
- Python
- Pydantic

## AI / ML

- Sentence Transformers
- Groq LLM API
- Retrieval Augmented Generation (RAG)

## Vector Database

- Qdrant

## Testing

- Pytest
- FastAPI TestClient

---

# Project Structure

```
Document Q&A Chatbot API
│
├── app
│   ├── main.py
│   └── config.py
│
├── api
│   └── routes.py
│
├── rag
│   ├── pipeline.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── loader.py
│   └── splitter.py
│
├── models
│   └── schemas.py
│
├── documents
│   └── uploaded files
│
├── vectorstore
│   └── Qdrant local database
│
├── tests
│   └── test_api.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd "Document Q&A Chatbot API"
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

---

# Running the API

Start FastAPI server:

```bash
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Upload Document

### POST

```
/ingest
```

Uploads a document and creates vector embeddings.

Example:

```json
{
    "filename": "document.txt"
}
```

---

# Chat Endpoint

### POST

```
/chat
```

Ask questions from uploaded documents.

Request:

```json
{
    "session_id": "user123",
    "query": "What is Retrieval Augmented Generation?"
}
```

Response:

```json
{
    "answer": "Retrieval Augmented Generation combines information retrieval with language generation...",
    "sources": [
        "Chunk 1",
        "Chunk 2"
    ]
}
```

---

# Streaming Chat

The API also supports streaming responses where generated tokens are returned progressively.

Endpoint:

```
/chat/stream
```

---

# RAG Implementation Details

## 1. Document Loading

Documents are loaded and converted into plain text.

Supported formats:

- TXT
- PDF

---

## 2. Text Chunking

Large documents are divided into smaller sections.

Benefits:

- Better retrieval accuracy
- Reduced context size
- Improved LLM performance

---

## 3. Embeddings

Text chunks are converted into numerical vectors using:

```
Sentence Transformers
(all-MiniLM-L6-v2)
```

These vectors represent semantic meaning rather than simple keyword matching.

---

## 4. Vector Storage

Qdrant stores:

- Embedding vectors
- Original text chunks
- Metadata information

Example metadata:

```
{
 "chunk_index": 5,
 "source": "document.txt"
}
```

---

## 5. Retrieval

When a user asks a question:

1. Query is converted into an embedding
2. Similar vectors are searched in Qdrant
3. Top relevant chunks are retrieved
4. Retrieved context is sent to the LLM

---

## 6. Generation

Groq LLM generates answers using only retrieved context.

The system follows a grounding rule:

```
If the answer is not present in the context,
reply:

I don't know.
```

This reduces hallucination.

---

# Conversation Memory

The chatbot maintains short-term conversation history.

Features:

- Session-based history
- Last 6 messages retained
- Previous context used during follow-up questions

Example:

User:

```
What is RAG?
```

Assistant:

```
Explanation...
```

User:

```
Why is it useful?
```

The chatbot understands the previous discussion.

---

# Response Caching

The system includes query caching.

Benefits:

- Faster repeated responses
- Reduced LLM API usage
- Improved performance

Cache keys are generated using:

```
MD5(session_id + query)
```

---

# Testing

Run:

```bash
pytest tests -v
```

The test suite covers:

- Document ingestion
- Chat responses
- Unknown questions
- Source retrieval
- Cache behaviour

---

# Future Improvements

Possible enhancements:

- Authentication system
- Multiple document collections
- User-specific knowledge bases
- Redis based caching
- Production Qdrant server deployment
- RAG evaluation using RAGAS
- Better document format support
- Hybrid search (keyword + semantic)

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Large Language Models
- Prompt Engineering
- Embeddings
- Semantic Search
- Vector Databases
- Retrieval Augmented Generation
- FastAPI API development
- AI application architecture

---

# Author

**Mubashra Noor**
