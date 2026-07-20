#Write a function semantic_search(query, documents) that embeds the query, embeds all documents, and returns the top-3 most similar documents with their cosine similarity scores.
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "FastAPI is a modern framework for building REST APIs.",
    "Flask is a lightweight Python web framework.",
    "Django includes an ORM and authentication system.",
    "TensorFlow is used for deep learning.",
    "Pandas helps analyze tabular data.",
    "Git tracks source code changes."
]

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

def semantic_search(query, documents, top_k=3):
    query_embedding = model.encode(query)
    doc_embeddings = model.encode(documents)

    scores = []

    for doc, emb in zip(documents, doc_embeddings):
        similarity = cosine_similarity(query_embedding, emb)
        scores.append((doc, similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_k]

query = "Which Python framework can I use to create APIs?"

results = semantic_search(query, documents)

for doc, score in results:
    print(f"{score:.4f} -> {doc}")