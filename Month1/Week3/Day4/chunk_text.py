"""
Practice Question 1

Write a chunk_text(text, chunk_size=500, overlap=50) function that splits a long string into overlapping chunks.
"""

from utils.chunking import chunk_text
from utils.document_loader import load_document


def main():

    document = load_document("data/sample.txt")

    # Simulate a much larger document (~3000 words)
    large_document = (" " + document) * 700

    chunks = chunk_text(
        large_document,
        chunk_size=500,
        overlap=50
    )

    print("=" * 60)
    print("Practice Question 1")
    print("=" * 60)

    print(f"Document Length : {len(large_document):,} characters")
    print(f"Total Chunks    : {len(chunks)}")

    print("\nPreview of First Chunk")
    print("-" * 60)
    print(chunks[0])

    print("\nPreview of Last Chunk")
    print("-" * 60)
    print(chunks[-1])


if __name__ == "__main__":
    main()