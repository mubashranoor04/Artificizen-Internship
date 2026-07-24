from rag.loader import load_document



text = load_document(
    "documents/test.txt"
)


print(text)
