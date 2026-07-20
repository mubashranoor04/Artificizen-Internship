#Write a utility embed_and_store(texts, metadata_list, collection) that batch-embeds a list of strings and upserts them into a Qdrant collection with metadata. You will reuse this directly in the RAG pipeline tomorrow.
from qdrant_client.models import PointStruct

def embed_and_store(
    client,
    collection_name,
    texts,
    metadata_list
):
    embeddings = model.encode(texts)

    points = []

    for i, (text, metadata, embedding) in enumerate(
        zip(texts, metadata_list, embeddings)
    ):
        points.append(
            PointStruct(
                id=i,
                vector=embedding.tolist(),
                payload={
                    "text": text,
                    **metadata
                }
            )
        )

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    print(f"Stored {len(points)} documents successfully.")