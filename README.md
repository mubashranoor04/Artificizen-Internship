# Artificizen AI Engineering Internship

This repository contains the **training work, hands-on exercises, and weekly capstone projects** completed during the initial phase of my **AI Engineering Internship at Artificizen**.

The first three weeks focused on building practical foundations in **Python, Object-Oriented Programming, backend development with FastAPI, Generative AI, prompt engineering, and Retrieval-Augmented Generation (RAG)**.

Each week followed a structured five-day learning cycle consisting of concepts, hands-on implementations, practice tasks, and a weekly capstone project.

> **Note:** This repository represents the structured training phase of the internship and does not contain all of the work completed throughout the internship.

---

## Training Overview

|  Week  | Focus Area                              | Weekly Capstone           |
| :----: | --------------------------------------- | ------------------------- |
| **01** | Python & Object-Oriented Programming    | Library Management System |
| **02** | FastAPI & Backend Development           | Task Management REST API  |
| **03** | Generative AI, Prompt Engineering & RAG | Document Q&A Chatbot API  |

---

# Week 1 — Python & Object-Oriented Programming

The first week focused on strengthening Python fundamentals and developing a solid understanding of **Object-Oriented Programming (OOP)** through practical implementation.

### Topics Covered

* Python fundamentals
* Data types and operators
* Conditional statements and loops
* Lists, tuples, dictionaries, and sets
* String manipulation
* Functions
* `*args` and `**kwargs`
* Lambda functions
* Functional programming tools
* Recursion
* Modules and imports
* Classes and objects
* Constructors and methods
* Encapsulation
* Properties
* Class methods and static methods
* Inheritance
* Polymorphism
* Abstraction
* Dunder methods
* Exception handling
* File handling
* JSON data persistence
* Virtual environments
* `pip` and `requirements.txt`
* Python type hints

### Weekly Capstone

#### Library Management System

A command-line application designed using object-oriented principles.

**Key implementation areas:**

* Book and library management
* Object-oriented design
* CLI-based interaction
* JSON-based data persistence
* Exception handling
* Structured Python code

---

# Week 2 — FastAPI & Backend Development

The second week transitioned from Python fundamentals into **backend development and REST API design using FastAPI**.

The focus was on building structured APIs, integrating databases, implementing authentication, and testing backend functionality.

### Topics Covered

* FastAPI fundamentals
* REST API architecture
* Path parameters
* Query parameters
* Pydantic models
* Request validation
* Response validation
* SQLAlchemy
* Database integration
* CRUD operations
* Database dependencies
* Alembic migrations
* Password hashing
* Authentication and authorization
* JWT authentication
* Role-Based Access Control (RBAC)
* Environment variables
* Secure configuration
* API routers
* Middleware
* CORS
* Global exception handling
* Background tasks
* Application lifespan
* API testing
* Pytest
* FastAPI TestClient

### Weekly Capstone

#### Task Management REST API

A backend application developed with FastAPI for managing users and tasks.

**Key implementation areas:**

* User registration and authentication
* JWT-based authorization
* Role-based access control
* Task CRUD operations
* Database integration
* Protected API routes
* Request and response validation
* Error handling
* Automated API testing

---

# Week 3 — Generative AI, Prompt Engineering & RAG

The third week focused on **Generative AI and Retrieval-Augmented Generation**, moving from LLM fundamentals to the implementation of a practical RAG-based application.

### Topics Covered

#### Generative AI & LLM Fundamentals

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Generative AI
* Large Language Models (LLMs)
* Transformer architecture
* Tokens
* Context windows
* LLM inference

#### Prompt Engineering

* Prompt structure
* Zero-shot prompting
* Few-shot prompting
* Role prompting
* Output control
* Prompt chaining
* Prompt injection
* Context management

#### Embeddings & Semantic Search

* Text embeddings
* Sentence Transformers
* `all-MiniLM-L6-v2`
* Semantic similarity
* Cosine similarity
* Vector representations
* Metadata filtering

#### Vector Databases

* Vector database concepts
* ChromaDB
* Qdrant
* Collection management
* Vector storage
* Similarity search

#### Retrieval-Augmented Generation

* RAG architecture
* Document loading
* Document processing
* Text chunking
* Embedding generation
* Vector indexing
* Semantic retrieval
* Context augmentation
* Grounded generation
* Retrieval pipelines
* Query pipelines

#### Application Development

* Groq API
* FastAPI integration
* Multi-turn conversations
* Conversation history
* Streaming responses
* Source citations
* Basic caching
* RAG evaluation
* Production-oriented ingestion and retrieval

### Weekly Capstone

#### Document Q&A Chatbot API

A **RAG-powered FastAPI application** designed to answer questions from uploaded documents using semantic retrieval and LLM-generated responses.

**Key implementation areas:**

* Document ingestion
* Document parsing and processing
* Text chunking
* Embedding generation
* Qdrant vector storage
* Semantic similarity search
* Metadata-based retrieval
* Groq LLM inference
* Context-aware question answering
* Multi-turn conversations
* Source citations
* Response streaming
* Basic response caching
* RAG evaluation

---

# Technology Stack

| Category                 | Technologies          |
| ------------------------ | --------------------- |
| **Programming Language** | Python                |
| **Backend**              | FastAPI, Uvicorn      |
| **Data Validation**      | Pydantic              |
| **Database**             | SQLite, SQLAlchemy    |
| **Database Migrations**  | Alembic               |
| **Authentication**       | JWT, OAuth2, bcrypt   |
| **LLM Inference**        | Groq                  |
| **Embeddings**           | Sentence Transformers |
| **Embedding Model**      | `all-MiniLM-L6-v2`    |
| **Vector Database**      | Qdrant                |
| **Vector DB Exercises**  | ChromaDB              |
| **Similarity Search**    | Cosine Similarity     |
| **Document Processing**  | PyMuPDF               |
| **RAG Evaluation**       | Ragas                 |
| **Testing**              | Pytest, HTTPX         |
| **Configuration**        | python-dotenv         |

---

# Repository Structure

The repository is organized according to the internship training progression:

```text
Artificizen-Internship/
│
├── Month 1/
│   │
│   ├── Week 1/
│   │   ├── Day 1/
│   │   ├── Day 2/
│   │   ├── Day 3/
│   │   ├── Day 4/
│   │   ├── Day 5/
│   │   └── Library Management System/
│   │
│   ├── Week 2/
│   │   ├── Day 1/
│   │   ├── Day 2/
│   │   ├── Day 3/
│   │   ├── Day 4/
│   │   ├── Day 5/
│   │   └── Task Management API/
│   │
│   └── Week 3/
│       ├── Day 1/
│       ├── Day 2/
│       ├── Day 3/
│       ├── Day 4/
│       ├── Day 5/
│       └── Document Q&A Chatbot/
│
└── README.md
```

---

# Learning Progression

The training followed a gradual progression from programming fundamentals to practical AI engineering:

```text
Python Fundamentals
        │
        ▼
Object-Oriented Programming
        │
        ▼
FastAPI & REST APIs
        │
        ▼
Databases & Authentication
        │
        ▼
Generative AI & LLM Fundamentals
        │
        ▼
Prompt Engineering
        │
        ▼
Embeddings & Semantic Search
        │
        ▼
Vector Databases
        │
        ▼
RAG Pipelines
        │
        ▼
FastAPI + RAG Application
```

This progression provided the technical foundation for working with backend systems and AI-powered applications later in the internship.

---

# Repository Scope

This repository is specifically intended to document the **structured training phase and personal implementations** completed during the initial weeks of the internship.

It does **not** represent the complete body of work completed during my internship.

The following are intentionally not included:

* Company-specific projects
* Team-based projects
* Client-related work
* Internal Artificizen projects
* Confidential implementations
* Proprietary company resources or data
* Other internship tasks that are not part of this training repository

These projects and tasks are kept separate where required due to their **company, team, client, or confidentiality scope**.

---

# Separate Main Project

The larger full-fledged application developed during the internship is maintained in a **separate repository**.

Keeping the projects separate allows this repository to remain focused on the structured training progression, while the main application has its own implementation, architecture, documentation, and project-specific details.

---

# Purpose

The purpose of this repository is to document the progression of my technical learning during the early stage of the **Artificizen AI Engineering Internship**.

It demonstrates the transition from:

**Python → Backend Development → Generative AI → RAG**

through hands-on implementation rather than theory alone.

The repository provides a structured record of the exercises, daily implementations, and capstone projects that formed the foundation for subsequent AI engineering work during the internship.

---

## Internship Focus

Throughout this training phase, the primary areas of development were:

* **Python Development**
* **Object-Oriented Programming**
* **Backend Engineering**
* **REST API Development**
* **Database Integration**
* **Authentication & Authorization**
* **Generative AI**
* **LLM Applications**
* **Prompt Engineering**
* **Embeddings**
* **Vector Databases**
* **Semantic Search**
* **Retrieval-Augmented Generation**
* **AI Application Development**

---

> **Artificizen AI Engineering Internship**
> Training Repository · Python · FastAPI · Generative AI · RAG
