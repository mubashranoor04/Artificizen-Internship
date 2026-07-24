import hashlib

from groq import Groq

from app.config import settings
from rag.embeddings import embedding_model
from rag.vector_store import vector_store


client = Groq(
    api_key=settings.GROQ_API_KEY
)


chat_history = {}
cache = {}


def ask(session_id, query):

    if session_id not in chat_history:
        chat_history[session_id] = []

    history = chat_history[session_id]


    cache_key = hashlib.md5(
        f"{session_id}:{query}".encode()
    ).hexdigest()


    if cache_key in cache:
        print("Cache HIT")
        return cache[cache_key]


    print("Cache MISS")


    query_vector = embedding_model.embed_text(query)


    results = vector_store.search(
        query_vector,
        limit=3
    )


    context = ""
    sources = []


    for i, result in enumerate(results):

        text = result.payload["text"]

        context += f"{i+1}. {text}\n\n"

        sources.append(
            f"Chunk {result.payload['chunk_index']}"
        )


    prompt = f"""

Use ONLY the context below.

If the answer is not present in the context,
reply exactly:

I don't know.

Context:

{context}


Question:

{query}

"""


    messages = [

        {
            "role": "system",
            "content":
            "Answer only using the provided context. "
            "If the answer is unavailable reply: I don't know."
        }

    ]


    messages.extend(history)


    messages.append(

        {
            "role":"user",
            "content":prompt
        }

    )


    response = client.chat.completions.create(

        model=settings.GROQ_MODEL,

        messages=messages,

        temperature=0

    )


    answer = response.choices[0].message.content



    history.append(

        {
            "role":"user",
            "content":query
        }

    )


    history.append(

        {
            "role":"assistant",
            "content":answer
        }

    )


    chat_history[session_id] = history[-6:]


    cache[cache_key] = (
        answer,
        sources
    )


    return answer, sources
def stream_answer(session_id, query):

    if session_id not in chat_history:
        chat_history[session_id] = []

    history = chat_history[session_id]


    query_vector = embedding_model.embed_text(query)


    results = vector_store.search(
        query_vector,
        limit=3
    )


    context = ""

    for i, result in enumerate(results):

        context += (
            f"{i+1}. "
            f"{result.payload['text']}\n\n"
        )


    prompt = f"""
Use ONLY the context below.

If the answer is not present in the context,
reply exactly:

I don't know.

Context:

{context}

Question:

{query}
"""


    messages = [

        {
            "role":"system",
            "content":
            "Answer only using the provided context."
        }

    ]


    messages.extend(history)


    messages.append(

        {
            "role":"user",
            "content":prompt
        }

    )


    stream = client.chat.completions.create(

        model=settings.GROQ_MODEL,

        messages=messages,

        temperature=0,

        stream=True

    )


    full_answer = ""


    for chunk in stream:

        if chunk.choices[0].delta.content:

            token = chunk.choices[0].delta.content

            full_answer += token

            yield token



    history.append(
        {
            "role":"user",
            "content":query
        }
    )


    history.append(
        {
            "role":"assistant",
            "content":full_answer
        }
    )


    chat_history[session_id] = history[-6:]