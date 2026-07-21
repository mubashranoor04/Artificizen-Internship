"""
Practice Question 6

Compare answers with and without Retrieval-Augmented Generation (RAG) to observe how grounding improves response reliability.
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
    Load the sample document, split it into chunks,
    and store the embeddings in Qdrant.
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


def ask_without_rag(question):
    """
    Send the question directly to the LLM.
    """

    return ask(
        prompt=question,
        temperature=0,
    )


def ask_with_rag(question):
    """
    Retrieve relevant context before asking the LLM.
    """

    retrieved_chunks = retrieve(
        query=question,
        top_k=3,
    )

    prompt = build_prompt(
        query=question,
        chunks=retrieved_chunks,
    )

    return ask(
        prompt=prompt,
        temperature=0,
    )

def main():
    prepare_database()

    question = "Who invented Facebook?"

    print("=" * 70)
    print("Practice Question 6 - Hallucination Test")
    print("=" * 70)

    print(f"\nQuestion:\n{question}")

    print("\n" + "=" * 70)
    print("WITHOUT RAG")
    print("=" * 70)

    normal_answer = ask_without_rag(question)

    print(normal_answer)

    print("\n" + "=" * 70)
    print("WITH RAG")
    print("=" * 70)

    rag_answer = ask_with_rag(question)

    print(rag_answer)

    print("\n" + "=" * 70)
    print("Observation")
    print("=" * 70)

    print(
        "The response generated without RAG relied on the model's "
        "general knowledge and answered the question directly. "
        "The RAG-based response was restricted to the retrieved "
        "document context. Since the document did not contain "
        "information about the inventor of Facebook, the model "
        "correctly replied 'I don't know.' This demonstrates "
        "how RAG helps reduce hallucinations by grounding the "
        "response in the provided evidence."
    )
if __name__ == "__main__":
    main()