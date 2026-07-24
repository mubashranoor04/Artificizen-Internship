import os

from rag.loader import load_document
from rag.splitter import chunk_text
from rag.embeddings import embedding_model
from rag.vector_store import vector_store


def ingest_document(file_path):

    text = load_document(file_path)

    chunks = chunk_text(text)

    vectors = embedding_model.embed_documents(chunks)

    try:
        vector_store.create_collection()
    except Exception:
        pass

    vector_store.add_documents(
        vectors=vectors,
        texts=chunks,
        source=os.path.basename(file_path)
    )

    return len(chunks)