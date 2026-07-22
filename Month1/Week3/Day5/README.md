# Day 5 – Retrieval-Augmented Generation (RAG)

# Overview

This project introduces the fundamentals of **Retrieval-Augmented Generation (RAG)** using open-source tools and local embeddings.

The objective of this practice was to understand how Large Language Models can retrieve relevant information from external documents before generating responses, resulting in more accurate and grounded answers.

The implementation focused on building a complete RAG pipeline including:

- Document Loading
- Text Chunking
- Embeddings Generation
- Vector Database Storage
- Semantic Search
- Question Answering
- Manual Evaluation
- RAGAS Evaluation

By completing this practice, I learned how to:

- Understand the architecture of Retrieval-Augmented Generation (RAG).
- Split large documents into meaningful chunks.
- Generate vector embeddings using Sentence Transformers.
- Store embeddings inside a Qdrant vector database.
- Perform semantic similarity search.
- Retrieve relevant context before generating answers.
- Build an end-to-end RAG question-answering pipeline.
- Evaluate RAG system performance using manual testing and RAGAS metrics.

---

# Technologies Used

- Python
- LangChain
- Sentence Transformers
- HuggingFace Embeddings
- Qdrant Vector Database
- Transformers
- RAGAS
- Datasets
- python-dotenv
- Virtual Environment (venv)

---

# Files Description

## chunks.py

### Objective

Understand how large documents are divided into smaller pieces before indexing.

### Concept

Large documents cannot be embedded efficiently as a single block.

Chunking divides text into smaller overlapping sections while preserving context.

### Implementation

- Loaded sample document
- Split text into chunks
- Applied chunk overlap
- Displayed generated chunks

### What I Learned

- Why chunking is necessary.
- Importance of chunk size.
- How overlap preserves context between chunks.

---

## embeddings.py

### Objective

Generate vector embeddings for text chunks.

### Concept

Embeddings convert text into high-dimensional numerical vectors that capture semantic meaning.

Similar text produces similar vectors.

### Implementation

- Loaded Sentence Transformer model.
- Generated embeddings for document chunks.
- Verified embedding dimensions.

### What I Learned

- Difference between text and vector representations.
- Semantic similarity using embeddings.
- Importance of embedding models in RAG.

---

## qdrant_store.py

### Objective

Store embeddings inside a vector database.

### Concept

Vector databases efficiently store and search embeddings using similarity search.

Qdrant enables fast nearest-neighbor retrieval.

### Implementation

- Created Qdrant collection.
- Inserted chunk embeddings.
- Stored metadata with vectors.

### What I Learned

- How vector databases work.
- Why metadata is stored alongside vectors.
- Basics of semantic indexing.

---

## rag_pipeline.py

### Objective

Build an end-to-end Retrieval-Augmented Generation pipeline.

### Concept

Instead of answering directly from model knowledge, the system first retrieves relevant document chunks.

Workflow:

```
Question
      ↓
Embedding
      ↓
Vector Search
      ↓
Relevant Chunks
      ↓
LLM
      ↓
Generated Answer
```

### Implementation

- Embedded user query.
- Retrieved relevant chunks from Qdrant.
- Combined retrieved context.
- Generated grounded answers.

### What I Learned

- Complete RAG workflow.
- Importance of retrieval before generation.
- How grounding reduces hallucinations.

---

## evaluation.py

### Objective

Evaluate the RAG pipeline manually.

### Concept

Manual evaluation compares generated responses with expected answers.

Each response is categorized as:

- Correct
- Partially Correct
- Wrong

### Implementation

- Prepared evaluation questions.
- Compared expected and generated answers.
- Calculated overall accuracy.

### What I Learned

- Importance of evaluating AI systems.
- How retrieval quality affects final answers.
- Basic performance measurement.

---

## ragas_eval.py

### Objective

Evaluate RAG performance using RAGAS.

### Concept

RAGAS provides automated metrics for Retrieval-Augmented Generation systems.

Common evaluation metrics include:

- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall

### Implementation

- Created evaluation dataset.
- Used RAGAS evaluation framework.
- Generated evaluation metrics.

### What I Learned

- Difference between manual and automated evaluation.
- Importance of objective RAG benchmarking.
- Measuring retrieval and generation quality.

---

# Environment Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks execution:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

---

## Install Dependencies

```bash
pip install langchain
pip install sentence-transformers
pip install qdrant-client
pip install transformers
pip install datasets
pip install ragas
pip install python-dotenv
```

Or install everything from:

```bash
pip install -r requirements.txt
```

---

# Concepts Learned

## Retrieval-Augmented Generation (RAG)

RAG combines document retrieval with language generation.

Instead of relying only on pretrained knowledge, the model retrieves relevant information before generating a response.

Benefits:

- More accurate answers
- Reduced hallucinations
- Knowledge can be updated without retraining

---

## Document Chunking

Documents are divided into smaller overlapping sections.

Benefits:

- Better retrieval accuracy
- Improved context preservation
- Faster indexing

---

## Embeddings

Embeddings transform text into numerical vectors.

Similar meanings produce similar vectors.

Applications:

- Semantic Search
- Recommendation Systems
- Question Answering

---

## Vector Databases

Vector databases store embeddings for efficient similarity search.

In this project, **Qdrant** was used to:

- Store vectors
- Perform nearest-neighbor search
- Retrieve relevant document chunks

---

## Semantic Search

Unlike keyword search, semantic search retrieves information based on meaning rather than exact words.

Advantages:

- Better understanding of user intent
- Improved retrieval quality
- More relevant search results

---

## Manual Evaluation

Manual evaluation compares expected answers with generated responses.

Possible outcomes:

- Correct
- Partially Correct
- Wrong

This provides a simple estimate of system accuracy.

---

## RAGAS Evaluation

RAGAS is an automated evaluation framework for Retrieval-Augmented Generation systems.

It measures:

- Faithfulness
- Answer Relevancy
- Context Precision
- Context Recall

These metrics help evaluate both retrieval quality and generated responses.

---

# Summary

By completing Day 5, I learned the complete workflow of building a Retrieval-Augmented Generation (RAG) application.

I implemented and explored:

- Document Loading
- Text Chunking
- Embeddings Generation
- Vector Database Integration
- Semantic Search
- Retrieval-Augmented Generation Pipeline
- Manual Evaluation
- RAGAS Evaluation

These concepts provide the foundation for building production-ready AI applications that use external knowledge sources to generate more accurate and reliable responses.