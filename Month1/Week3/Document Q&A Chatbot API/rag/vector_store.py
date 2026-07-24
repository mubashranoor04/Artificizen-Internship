from qdrant_client import QdrantClient
from qdrant_client.models import (
    VectorParams,
    Distance,
    PointStruct,
)


class VectorStore:

    def __init__(self):

        self.client = QdrantClient(path="vectorstore")

        self.collection_name = "documents"

    def create_collection(self):

        self.client.create_collection(
            collection_name=self.collection_name,
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE,
            ),
        )

    def add_documents(
        self,
        vectors,
        texts,
        source="document.txt",
    ):

        points = []

        for index, vector in enumerate(vectors):

            points.append(
                PointStruct(
                    id=index,
                    vector=vector.tolist(),
                    payload={
                        "text": texts[index],
                        "chunk_index": index,
                        "source": source,
                    },
                )
            )

        self.client.upsert(
            collection_name=self.collection_name,
            points=points,
        )

    def search(
        self,
        vector,
        limit=3,
    ):

        results = self.client.query_points(
            collection_name=self.collection_name,
            query=vector.tolist(),
            limit=limit,
        )

        return results.points


vector_store = VectorStore()