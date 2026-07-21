# Day 4 – Retrieval-Augmented Generation (RAG) Pipeline

## Overview

This project introduces the fundamentals of Retrieval-Augmented Generation (RAG), a modern AI architecture that combines Large Language Models (LLMs) with external knowledge retrieval.

Unlike traditional LLM applications that rely only on pre-trained model knowledge, RAG systems retrieve relevant information from external documents and provide that context to the language model before generating responses.

Throughout this practice, I explored how modern AI systems process documents, convert text into embeddings, store vectors inside databases, retrieve relevant information, and prepare context for LLM-based question answering.

The implementation focused on:

- Document Loading
- Text Extraction
- Text Chunking
- Embedding Generation
- Vector Storage
- Similarity Search
- Context Retrieval
- RAG Pipeline Design

By completing this practice, I learned how to:

- Load and process different document formats such as TXT and PDF.
- Extract meaningful text for AI processing.
- Split large documents into smaller searchable chunks.
- Generate embeddings using sentence transformer models.
- Store embeddings inside vector databases.
- Retrieve relevant information using semantic similarity.
- Build the retrieval layer required for RAG applications.


---

# Technologies Used

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- NumPy
- Qdrant
- ChromaDB
- PyMuPDF / pymupdf4llm
- Vector Embeddings
- Retrieval-Augmented Generation (RAG)
- Virtual Environment (venv)


---

# Project Structure

```
Day4/

│
├── requirements.txt
├── README.md
│
├── utils/
│   ├── document_loader.py
│   ├── text_splitter.py
│   └── embedding_utils.py
│
├── q1_document_loading.py
├── q2_text_chunking.py
├── q3_embed_documents.py
├── q4_store_vectors.py
├── q5_retrieve_context.py
└── q6_rag_pipeline.py
```

---

# Files Description


## q1_document_loading.py

### Objective

Understand how documents are loaded and converted into plain text before being processed inside an AI pipeline.

### Concept

AI systems cannot directly understand files such as PDFs and text documents.

The first stage of a RAG pipeline is converting different document formats into clean text that can later be transformed into embeddings.

### Implementation

- Loaded TXT documents.
- Extracted text from PDF files.
- Created reusable document loading utilities.
- Prepared documents for further processing.

### What I Learned

- Documents must be converted into text before embedding.
- Different file formats require different extraction techniques.
- Reusable loaders improve the scalability of AI systems.


---

## q2_text_chunking.py

### Objective

Understand why large documents need to be divided into smaller sections before generating embeddings.

### Concept

Large documents may exceed the context limits of language models.

Chunking divides documents into smaller meaningful sections that can be individually embedded, stored, and retrieved.

Process:

```
Large Document
      |
      v
Document Chunks
      |
      v
Embeddings
      |
      v
Vector Database
```

### Implementation

- Created a text splitting utility.
- Defined chunk size and overlap.
- Generated smaller document sections.
- Prepared chunks for embedding generation.

### What I Learned

- Chunk size directly affects retrieval quality.
- Chunk overlap helps preserve context between sections.
- Effective chunking improves RAG performance.


---

## q3_embed_documents.py

### Objective

Generate vector embeddings for document chunks using a sentence transformer model.

### Concept

Embeddings convert text into numerical vector representations that capture semantic meaning.

These vectors allow AI systems to compare information based on meaning rather than exact keyword matching.

### Implementation

- Loaded the all-MiniLM-L6-v2 model.
- Generated embeddings for document chunks.
- Converted text into numerical representations.
- Prepared vectors for database storage.

### What I Learned

- Embeddings create a connection between human language and machine-readable representations.
- Similar meanings produce similar vector representations.
- Embedding models are a core component of RAG systems.


---

## q4_store_vectors.py

### Objective

Store document embeddings inside a vector database for efficient semantic retrieval.

### Concept

Vector databases are designed to store high-dimensional embeddings and perform similarity searches.

Instead of searching through plain text, they compare numerical representations of meaning.

### Implementation

- Created a Qdrant collection.
- Stored document embeddings.
- Attached original text and metadata.
- Performed vector insertion operations.

### What I Learned

- Vector databases enable efficient semantic retrieval.
- Documents should be stored with embeddings and metadata.
- Qdrant is suitable for production-level AI applications.


---

## q5_retrieve_context.py

### Objective

Retrieve the most relevant document chunks for a user query.

### Concept

A RAG system first retrieves relevant information from a vector database before generating an answer.

The user query is converted into an embedding and compared against stored document embeddings.

### Implementation

- Converted user queries into embeddings.
- Performed similarity search.
- Retrieved the most relevant chunks.
- Prepared retrieved context for the language model.

### What I Learned

- Retrieval quality directly impacts AI response accuracy.
- Semantic search provides better results than keyword matching.
- Relevant context reduces incorrect model responses.


---

## q6_rag_pipeline.py

### Objective

Combine document processing, embedding generation, storage, and retrieval into a complete RAG workflow.

### Concept

A complete RAG pipeline follows these stages:

```
Documents
    |
    v
Text Extraction
    |
    v
Chunking
    |
    v
Embedding Generation
    |
    v
Vector Database
    |
    v
Similarity Retrieval
    |
    v
LLM Response Generation
```

### Implementation

- Created an end-to-end RAG workflow.
- Connected document loading utilities.
- Generated document embeddings.
- Stored vectors in a database.
- Retrieved relevant information.
- Prepared context for LLM integration.

### What I Learned

- RAG combines retrieval systems with language models.
- Each pipeline component contributes to response quality.
- Modular design makes AI applications easier to maintain and scale.


---

# Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If execution is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

## Install Dependencies

```bash
pip install -r requirements.txt
```


---

# Concepts Learned


## Retrieval-Augmented Generation (RAG)

RAG is an AI architecture that improves LLM responses by retrieving external information before generating answers.

Instead of depending only on model memory, RAG provides additional context from external sources.

Benefits:

- More accurate responses
- Domain-specific knowledge
- Reduced hallucination
- Ability to use private data


---

## Document Processing

Before documents can be searched, they must go through several processing stages:

1. Loading
2. Text Extraction
3. Cleaning
4. Chunking
5. Embedding Generation

Document processing is the foundation of every RAG system.


---

## Text Chunking

Chunking divides large documents into smaller searchable sections.

Important factors include:

- Chunk size
- Chunk overlap
- Document structure

Good chunking improves retrieval accuracy by ensuring relevant information can be found efficiently.


---

## Vector Databases

Vector databases store embeddings and enable similarity-based retrieval.

Examples:

- Qdrant
- ChromaDB

Key features:

- Vector similarity search
- Metadata storage
- Filtering capabilities
- Scalable retrieval


---

## Embedding Pipeline

The embedding pipeline converts text into numerical vectors.

Process:

```
Text
 |
 v
Embedding Model
 |
 v
Vector Representation
 |
 v
Vector Database
```


---

## Similarity Search

Similarity search identifies documents whose embeddings are closest to the query embedding.

The closer two vectors are, the more semantically related the information is.


---

## RAG Workflow

A complete RAG workflow:

1. User submits a query.
2. Query is converted into an embedding.
3. Vector database searches similar documents.
4. Relevant chunks are retrieved.
5. Retrieved context is provided to the LLM.
6. LLM generates a grounded response.


---

# Summary

By completing Day 4, I gained practical experience building the retrieval foundation of a Retrieval-Augmented Generation system.

I implemented and explored:

- Document Loading
- PDF and Text Extraction
- Text Chunking
- Embedding Generation
- Vector Storage
- Semantic Retrieval
- RAG Pipeline Architecture
- Reusable AI Utilities

These concepts form the core retrieval layer required for modern AI applications.

The next stage focuses on integrating the complete RAG pipeline with LLM inference using Groq and building an end-to-end question answering system.