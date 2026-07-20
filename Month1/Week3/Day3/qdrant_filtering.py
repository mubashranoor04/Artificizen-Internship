#Repeat the previous exercise using Qdrant (QdrantClient(':memory:')). Add payloads with a source field and filter results to only return documents where source == 'manual'.
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = QdrantClient(":memory:")

client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)
documents = [
    "Python basics Manual",
    "FastAPI Installation Guide",
    "Machine learning Research Notes"
]
sources = [
    "manual",
    "manual",
    "blog"
]
vectors = model.encode(documents)

points = []

for i, (doc, src, vec) in enumerate(zip(documents, sources, vectors)):
    points.append(
        PointStruct(
            id=i,
            vector=vec.tolist(),
            payload={
                "source": src,
                "text": doc
            }
        )
    )
client.upsert(
    collection_name="docs",
    points=points
)
query_vector = model.encode("API framework")

results = client.search(
    collection_name="docs",
    query_vector=query_vector.tolist(),
    query_filter=Filter(
        must=[
            FieldCondition(
                key="source",
                match=MatchValue(value="manual")
            )
        ]
    ),
    limit=2
)
for item in results:
    print(item.payload)