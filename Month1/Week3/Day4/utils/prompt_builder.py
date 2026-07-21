"""
Utility function for constructing a grounded RAG prompt.
"""

def build_prompt(query, chunks):
    """
    Build a prompt by combining retrieved document chunks
    with the user's question.

    Args:
        query (str): User question.
        chunks (list): Retrieved Qdrant points or plain text chunks.

    Returns:
        str: Prompt ready to send to the LLM.
    """

    context_sections = []

    for index, chunk in enumerate(chunks, start=1):

        # Supports both Qdrant results and plain strings
        if hasattr(chunk, "payload"):
            text = chunk.payload["text"]
        else:
            text = chunk

        context_sections.append(
            f"Context {index}:\n{text}"
        )

    context = "\n\n".join(context_sections)

    prompt = f"""
You are a question-answering assistant.

Use ONLY the information provided in the context below.

If the answer cannot be found in the context,
reply exactly with:

I don't know.

CONTEXT

{context}

QUESTION

{query}

ANSWER
"""

    return prompt.strip()


if __name__ == "__main__":

    sample_chunks = [
        "Python is a programming language.",
        "It is commonly used in Artificial Intelligence."
    ]

    question = "What is Python used for?"

    print(build_prompt(question, sample_chunks))