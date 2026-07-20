# Day 3 – Embeddings & Semantic Search

---

# Overview

This project introduces the fundamentals of **Embeddings**, **Semantic Search**, and **Vector Databases**, which form the foundation of Retrieval-Augmented Generation (RAG) systems.

Unlike traditional keyword search, semantic search understands the **meaning** and **context** of text by converting it into numerical vector representations called **embeddings**.

Throughout this practice, I explored how modern AI systems retrieve relevant information using vector similarity instead of exact keyword matching.

The implementation focused on experimenting with:

- Sentence Embeddings
- Cosine Similarity
- Semantic Search
- ChromaDB
- Qdrant
- Metadata Filtering
- Batch Embedding & Storage

By completing this practice, I learned how to:

- Generate sentence embeddings using Sentence Transformers.
- Compare text similarity using cosine similarity.
- Perform semantic document retrieval.
- Store embeddings inside vector databases.
- Filter search results using metadata.
- Build reusable embedding utilities for future RAG pipelines.

---

# Technologies Used

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- NumPy
- ChromaDB
- Qdrant
- Virtual Environment (venv)

---

# Project Structure

```
Day3/
│
├── requirements.txt
├── README.md
│
├── q1_embeddings_similarity.py
├── q2_semantic_search.py
├── q3_chromadb_search.py
├── q4_qdrant_filtering.py
├── q5_semantic_search_paraphrases.py
└── q6_embed_and_store.py
```

---

# Files Description

## q1_embeddings_similarity.py

### Objective

Understand how sentence embeddings capture semantic meaning by comparing multiple sentences using cosine similarity.

### Concept

Embeddings convert text into high-dimensional numerical vectors where semantically similar sentences are positioned closer together.

Instead of comparing words directly, similarity is measured between vectors.

### Implementation

- Loaded the **all-MiniLM-L6-v2** embedding model.
- Generated embeddings for six different sentences.
- Calculated cosine similarity for every sentence pair.
- Ranked all pairs from highest to lowest similarity.

### What I Learned

- Similar meaning produces similar embeddings.
- Embeddings capture context rather than exact wording.
- Cosine similarity is an effective metric for comparing vectors.

---

## q2_semantic_search.py

### Objective

Implement a basic semantic search function that retrieves the most relevant documents for a given query.

### Concept

Semantic search compares the embedding of a query with document embeddings instead of relying on keyword matching.

This allows documents with different wording but similar meaning to be retrieved successfully.

### Implementation

- Embedded the query.
- Embedded all documents.
- Computed cosine similarity scores.
- Returned the top three most similar documents.

### What I Learned

- Queries do not need exact keywords.
- Semantic similarity improves search quality.
- Embedding-based retrieval forms the core of RAG systems.

---

## q3_chromadb_search.py

### Objective

Learn how to store embeddings inside an in-memory ChromaDB collection and retrieve relevant documents.

### Concept

ChromaDB is a vector database that stores embeddings and performs similarity search efficiently.

Unlike relational databases, ChromaDB searches vectors rather than plain text.

### Implementation

- Created an in-memory ChromaDB collection.
- Added document embeddings.
- Queried the collection using a natural language question.
- Retrieved the two most relevant paragraphs.

### What I Learned

- Vector databases simplify semantic retrieval.
- ChromaDB automatically performs nearest-neighbor searches.
- Embeddings can be stored alongside original documents.

---

## q4_qdrant_filtering.py

### Objective

Understand vector search with metadata filtering using Qdrant.

### Concept

Qdrant stores both embeddings and additional metadata called payloads.

Metadata allows search results to be filtered before similarity ranking.

Example:

```
source = "manual"
```

Only documents matching the filter are returned.

### Implementation

- Created an in-memory Qdrant collection.
- Stored embeddings with metadata.
- Applied metadata filtering.
- Retrieved only documents originating from manuals.

### What I Learned

- Metadata improves retrieval precision.
- Payload filtering is essential for production RAG systems.
- Qdrant combines semantic search with structured filtering.

---

## q5_semantic_search_paraphrases.py

### Objective

Verify that semantic search retrieves relevant information even when different wording is used.

### Concept

Embeddings capture meaning instead of exact vocabulary.

For example:

Stored sentence:

```
A physician completed a successful heart surgery.
```

Query:

```
A doctor performed an operation.
```

Although the words differ, semantic search should identify them as highly related.

### Implementation

- Embedded fifty diverse sentences.
- Queried using paraphrased sentences.
- Compared similarity scores.
- Verified that semantically similar documents ranked highest.

### What I Learned

- Semantic search understands paraphrases.
- Exact keyword matching is not required.
- Embedding models generalize across different vocabulary.

---

## q6_embed_and_store.py

### Objective

Create a reusable utility for embedding multiple documents and storing them inside Qdrant.

### Concept

Real-world AI systems often ingest thousands of documents at once.

Rather than embedding documents individually, they are processed in batches and stored together with metadata.

### Implementation

- Created a reusable `embed_and_store()` function.
- Embedded multiple text documents.
- Attached metadata to every document.
- Upserted vectors into a Qdrant collection.

### What I Learned

- Utility functions reduce code duplication.
- Batch embedding improves efficiency.
- This function will be reused directly in the RAG pipeline.

---

# Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

If execution is blocked:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Concepts Learned

## Embeddings

Embeddings convert text into dense numerical vectors that preserve semantic meaning.

Unlike keywords, embeddings capture context and relationships between words.

---

## Sentence Transformers

Sentence Transformers generate high-quality sentence embeddings suitable for:

- Semantic Search
- Document Retrieval
- Question Answering
- Recommendation Systems

The model used in this project is:

```
all-MiniLM-L6-v2
```

It is lightweight, fast, and commonly used for RAG applications.

---

## Cosine Similarity

Cosine similarity measures the angle between two vectors.

Its values range from:

- **1** → Identical meaning
- **0** → Unrelated
- **-1** → Opposite direction (rare for sentence embeddings)

Higher similarity indicates stronger semantic relationships.

---

## Semantic Search

Traditional search relies on exact keywords.

Semantic search compares vector representations to retrieve documents with similar meanings.

Example:

Query:

```
A doctor treated a patient.
```

Retrieved document:

```
A physician completed a successful surgery.
```

Although the wording differs, the semantic meaning is similar.

---

## ChromaDB

ChromaDB is an open-source vector database used to store embeddings and perform similarity searches.

Key features:

- In-memory collections
- Persistent storage
- Fast vector retrieval
- Simple Python integration

---

## Qdrant

Qdrant is a production-ready vector database designed for semantic search and Retrieval-Augmented Generation (RAG).

Features include:

- High-performance vector search
- Metadata filtering
- Payload storage
- Scalable collections

---

## Metadata Filtering

Metadata provides additional information alongside stored vectors.

Examples include:

- Source
- Author
- Date
- Category
- Document ID

Filtering allows searches to be limited before similarity ranking.

Example:

```
source = "manual"
```

---

## Batch Embedding

Instead of embedding documents individually, large datasets are processed in batches.

Benefits:

- Faster ingestion
- Better scalability
- Reduced code duplication
- Easier integration into RAG systems

---

# Summary

By completing Day 3, I gained practical experience with the core technologies behind semantic search and Retrieval-Augmented Generation (RAG).

I implemented and explored:

- Sentence Embeddings
- Cosine Similarity
- Semantic Search
- ChromaDB
- Qdrant
- Metadata Filtering
- Batch Embedding Utilities

These concepts provide the foundation required for the next stage of development, where embeddings and vector databases will be integrated into a complete **Retrieval-Augmented Generation (RAG)** pipeline using Groq and FastAPI.