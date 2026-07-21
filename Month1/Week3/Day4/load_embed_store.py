"""
Practice Question 2

Load a document, chunk it,
embed every chunk,
store it in Qdrant.
"""

from utils.document_loader import load_document
from utils.chunking import chunk_text
from utils.qdrant_helper import create_collection, store_chunks


def main():

    document = load_document("data/sample.txt")

    chunks = chunk_text(document)

    create_collection()

    store_chunks(
        chunks=chunks,
        source="sample.txt",
    )

    print("=" * 60)
    print("Practice Question 2")
    print("=" * 60)

    print(f"Loaded Chunks : {len(chunks)}")
    print("Embeddings generated successfully.")
    print("Chunks stored in Qdrant.")


if __name__ == "__main__":
    main()