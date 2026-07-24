from rag.embeddings import embedding_model



sentence = (
    "Machine learning learns patterns from data"
)


vector = embedding_model.embed_text(
    sentence
)


print(
    "Vector size:",
    len(vector)
)


print(
    vector[:10]
)