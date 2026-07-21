"""
Practice Question 3

Retrieve top-k chunks
using semantic search.
"""

from utils.document_loader import load_document
from utils.chunking import chunk_text
from utils.qdrant_helper import (
    create_collection,
    store_chunks,
    retrieve,
)
def main():

    document = load_document("data/sample.txt")

    chunks = chunk_text(document)

    create_collection()

    store_chunks(
        chunks,
        source="sample.txt",
    )
    question = "What is Retrieval-Augmented Generation?"

    results = retrieve(
        question,
        top_k=3,
    )
    print("=" * 60)
    print("Practice Question 3")
    print("=" * 60)

    print(f"Query : {question}")

    print("\nTop Matches\n")

    for rank, result in enumerate(results, start=1):

        print("-" * 60)
        print(f"Rank : {rank}")
        print(f"Score : {result.score:.4f}")
        print(f"Source : {result.payload['source']}")
        print(f"Chunk : {result.payload['chunk_index']}")
        print()
        print(result.payload["text"])

if __name__ == "__main__":
    main()