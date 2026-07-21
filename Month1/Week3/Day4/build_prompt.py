"""
Practice Question 4

Build a grounded prompt
using retrieved document chunks.
"""

from utils.document_loader import load_document
from utils.chunking import chunk_text
from utils.qdrant_helper import (
    create_collection,
    store_chunks,
    retrieve,
)
from utils.prompt_builder import build_prompt

def main():

    # Load sample document
    document = load_document("data/sample.txt")

    # Split into chunks
    chunks = chunk_text(document)

    # Create database
    create_collection()

    # Store document
    store_chunks(
        chunks=chunks,
        source="sample.txt",
    )
    # Ask a question
    query = "What is Retrieval-Augmented Generation?"

    # Retrieve similar chunks
    retrieved_chunks = retrieve(
        query=query,
        top_k=3,
    )

    # Build prompt
    prompt = build_prompt(
        query=query,
        chunks=retrieved_chunks,
    )

    print("=" * 70)
    print("Practice Question 4")
    print("=" * 70)
    print(prompt)

if __name__ == "__main__":
    main()