from rag.pipeline import ask

answer, sources = ask(
    "test_session",
    "What is RAG?"
)

print(answer)

print(sources)