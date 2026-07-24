from rag.embeddings import embedding_model

import numpy as np



sentences = [

    "A dog is chasing a ball",

    "A puppy is playing outside",

    "I love eating pizza"

]



vectors = embedding_model.embed_documents(
    sentences
)



def cosine_similarity(
    a,
    b
):

    return np.dot(a,b) / (
        np.linalg.norm(a) *
        np.linalg.norm(b)
    )



for i in range(len(sentences)):

    for j in range(i+1,len(sentences)):

        score = cosine_similarity(
            vectors[i],
            vectors[j]
        )


        print(
            "\n"
            + sentences[i]
            + "\nVS\n"
            + sentences[j]
        )


        print(
            "Similarity:",
            score
        )
        