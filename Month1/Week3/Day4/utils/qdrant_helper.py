"""
Helper functions for creating a Qdrant collection,
storing document embeddings, and retrieving similar chunks.
"""

from pathlib import Path

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from utils.embeddings import embed_documents, embed_text

# Configuration

COLLECTION_NAME = "rag_documents"
VECTOR_SIZE = 384  # Embedding dimension for all-MiniLM-L6-v2

# Create database directory if it doesn't exist
DB_PATH = Path("db")
DB_PATH.mkdir(exist_ok=True)

# Initialize persistent local Qdrant database
client = QdrantClient(path=str(DB_PATH))


def create_collection():
    """
    Create a fresh collection for the current run.
    """

    existing = [
        collection.name
        for collection in client.get_collections().collections
    ]

    if COLLECTION_NAME in existing:
        client.delete_collection(COLLECTION_NAME)

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=VECTOR_SIZE,
            distance=Distance.COSINE,
        ),
    )


def store_chunks(chunks, source):
    """
    Generate embeddings for document chunks and store them in Qdrant.

    Args:
        chunks (list[str]): List of document chunks.
        source (str): Source filename.
    """

    embeddings = embed_documents(chunks)

    points = []

    for index, (chunk, embedding) in enumerate(zip(chunks, embeddings), start=1):

        points.append(
            PointStruct(
                id=index,
                vector=embedding.tolist(),
                payload={
                    "text": chunk,
                    "source": source,
                    "chunk_index": index,
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    print(f"Stored {len(points)} chunks from '{source}'.")


def retrieve(query, top_k=3):
    """
    Retrieve the most relevant document chunks for a user query.

    Args:
        query (str): User question.
        top_k (int): Number of chunks to retrieve.

    Returns:
        list: Retrieved Qdrant points.
    """

    query_vector = embed_text(query)

    search_result = client.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector.tolist(),
        limit=top_k,
    )

    return search_result.points


if __name__ == "__main__":

    create_collection()

    print("Qdrant helper initialized successfully.")