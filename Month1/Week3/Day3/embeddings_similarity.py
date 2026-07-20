#Use sentence-transformers with all-MiniLM-L6-v2 to embed "A dog is chasing a ball" and five other sentences. Compute cosine similarity between all pairs using NumPy and rank them from most to least similar.
from sentence_transformers import SentenceTransformer
import numpy as np

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Sentences
sentences = [
    "A dog is chasing a ball",          
    "A violinist rehearses before the evening concert.",
    "Heavy rain flooded the downtown streets overnight.",
    "A baker carefully decorates a three-layer chocolate cake.",
    "Researchers discovered a new coral reef ecosystem.",
    "The astronaut repaired a damaged satellite during the mission."
]

# Generate embeddings
embeddings = model.encode(sentences)

# Cosine similarity function
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

# Calculate similarities
results = []

for i in range(len(sentences)):
    for j in range(i + 1, len(sentences)):
        score = cosine_similarity(embeddings[i], embeddings[j])
        results.append((sentences[i], sentences[j], score))

# Sort from highest similarity to lowest
results.sort(key=lambda x: x[2], reverse=True)

print("Sentence Similarities:\n")

for s1, s2, score in results:
    print(f"{score:.4f}")
    print(f"  {s1}")
    print(f"  {s2}")
    print("-" * 50)