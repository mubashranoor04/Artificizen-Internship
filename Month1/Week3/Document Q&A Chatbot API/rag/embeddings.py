from sentence_transformers import SentenceTransformer


class EmbeddingModel:


    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )


    def embed_text(
        self,
        text
    ):

        vector = self.model.encode(
            text
        )

        return vector



    def embed_documents(
        self,
        documents
    ):

        vectors = self.model.encode(
            documents
        )

        return vectors



embedding_model = EmbeddingModel()