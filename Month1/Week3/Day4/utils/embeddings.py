"""
Sentence Transformer helper functions.
"""

from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def embed_text(text):
    """
    Generate an embedding for a single string.
    """
    return model.encode(text)


def embed_documents(documents):
    """
    Generate embeddings for multiple documents.
    """
    return model.encode(documents)


if __name__ == "__main__":

    sample_documents = [
        "Python is a programming language.",
        "Artificial Intelligence is changing industries.",
        "RAG combines retrieval with generation."
    ]

    vectors = embed_documents(sample_documents)

    print(f"Generated {len(vectors)} embeddings.")
    print(f"Embedding dimension: {len(vectors[0])}")