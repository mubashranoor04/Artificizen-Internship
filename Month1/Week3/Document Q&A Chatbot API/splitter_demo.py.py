from rag.splitter import chunk_text



text = """
Artificial Intelligence is a branch of computer science that focuses on creating
systems capable of performing tasks that normally require human intelligence.

Machine Learning is a subset of artificial intelligence where computers learn
patterns from data instead of being explicitly programmed.

Deep Learning is a specialized area of machine learning that uses artificial
neural networks inspired by the human brain.

Generative AI is a type of artificial intelligence that can create new content
including text, images, audio, and videos.

Large Language Models are deep learning models trained on massive amounts of
text data. They understand language patterns and generate human-like responses.

Retrieval Augmented Generation combines information retrieval with language
models. It allows LLMs to access external knowledge sources and generate
grounded answers.
""" * 5


chunks = chunk_text(
    text,
    chunk_size=100,
    overlap=20
)


print(
    "Number of chunks:",
    len(chunks)
)


for index, chunk in enumerate(chunks):

    print("\nCHUNK", index)

    print(chunk)