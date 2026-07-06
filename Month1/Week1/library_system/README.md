# Library Management System (CLI)

A production-grade, modular Command Line Interface (CLI) application built with Python. This system showcases core Object-Oriented Programming (OOP) architectures, clean separation of concerns, custom domain exception frameworks, and performant data indexing structures using standard JSON persistence.

## System Architecture & Project Structure

The project strictly follows professional software engineering practices by decoupling data schemas, business logic, and user interface layers.

```text
library_system/
│
├── data/
│   └── library_storage.json      # Persistence tier (Auto-generated on initialization)
│
├── src/
│   ├── exceptions.py             # Custom domain exception management hierarchy
│   ├── models.py                 # Structural blueprints (Book and Member data entities)
│   └── manager.py                # Core application engine and state serialization logic
│
├── main.py                       # Application execution gateway & CLI boundary
├── requirements.txt              # Dependency manifesto
└── README.md                     # Project documentation