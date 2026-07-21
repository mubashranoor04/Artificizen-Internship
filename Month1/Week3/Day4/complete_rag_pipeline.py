"""
Practice Question 5

Complete Retrieval-Augmented Generation (RAG) pipeline.

Pipeline:
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
Build Prompt
    ↓
Groq
    ↓
Answer
"""

from utils.ask import ask
from utils.chunking import chunk_text
from utils.document_loader import load_document
from utils.prompt_builder import build_prompt
from utils.qdrant_helper import (
    create_collection,
    retrieve,
    store_chunks,
)

def prepare_database():
    """
    Load the document and store it in Qdrant.
    """

    document = load_document("data/sample.txt")

    chunks = chunk_text(
        document,
        chunk_size=500,
        overlap=50,
    )

    create_collection()

    store_chunks(
        chunks=chunks,
        source="sample.txt",
    )


def answer_question(question):
    """
    Retrieve relevant chunks and generate an answer.
    """

    retrieved_chunks = retrieve(
        query=question,
        top_k=3,
    )

    prompt = build_prompt(
        query=question,
        chunks=retrieved_chunks,
    )

    response = ask(
        prompt=prompt,
        temperature=0,
    )
    return response

def main():
    prepare_database()
    questions = [
        "What is Python?",
        "What is Retrieval-Augmented Generation (RAG)?",
        "Who invented Facebook?"
    ]
    print("=" * 70)
    print("Practice Question 5 - Complete RAG Pipeline")
    print("=" * 70)

    for index, question in enumerate(questions, start=1):

        print(f"\nQuestion {index}")
        print("-" * 70)
        print(question)

        answer = answer_question(question)

        print("\nAnswer")
        print("-" * 70)
        print(answer)

if __name__ == "__main__":
    main()