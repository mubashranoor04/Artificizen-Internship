from rag.ingest import ingest_document

count = ingest_document(
    "documents/test.txt"
)

print(f"{count} chunks stored.")