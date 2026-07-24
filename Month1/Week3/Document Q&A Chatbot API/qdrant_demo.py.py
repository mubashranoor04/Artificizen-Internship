from rag.embeddings import embedding_model
from rag.vector_store import vector_store

documents = [

    "Artificial Intelligence allows computers to perform tasks that normally require human intelligence.",

    "Machine Learning enables computers to learn patterns from data.",

    "Retrieval Augmented Generation combines document retrieval with large language models.",

    "Deep Learning uses neural networks inspired by the human brain."

]

# Step 1:
# Convert documents into vectors

vectors = embedding_model.embed_documents(
    documents
)

print(
    "Created vectors:",
    len(vectors)
)

# Step 2:
# Create Qdrant collection

vector_store.create_collection()

print(
    "Qdrant collection created"
)
# Step 3:
# Store vectors

vector_store.add_documents(
    vectors,
    documents
)
print(
    "Documents stored successfully"
)

# Step 4:
# Search

query = (
    "How do LLMs use external documents?"
)
query_vector = embedding_model.embed_text(
    query
)

results = vector_store.search(
    query_vector,
    limit=2
)

print("\nSearch Results:\n")

for result in results:

    print(
        "Score:",
        result.score
    )

    print(
        "Text:",
        result.payload["text"]
    )

    print(
        "Chunk:",
        result.payload["chunk_index"]
    )

    print("----------------")