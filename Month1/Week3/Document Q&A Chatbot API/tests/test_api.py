import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)
import io

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_ingest_text_file():

    content = (
        "Retrieval Augmented Generation combines "
        "information retrieval with language models."
    )

    response = client.post(

        "/ingest",

        files={
            "file": (
                "test.txt",
                io.BytesIO(content.encode()),
                "text/plain",
            )
        },

    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Document ingested successfully"

    assert data["chunks"] >= 1


def test_chat_known_question():

    response = client.post(

        "/chat",

        json={
            "session_id": "pytest",
            "query": "What is Retrieval Augmented Generation?"
        }

    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data

    assert len(data["answer"]) > 0


def test_chat_unknown_question():

    response = client.post(

        "/chat",

        json={
            "session_id": "pytest",
            "query": "Who invented the iPhone?"
        }

    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data


def test_sources_returned():

    response = client.post(

        "/chat",

        json={
            "session_id": "pytest",
            "query": "What is Retrieval Augmented Generation?"
        }

    )

    data = response.json()

    assert isinstance(data["sources"], list)

    assert len(data["sources"]) > 0


def test_cache_hit():

    payload = {
        "session_id": "cache_user",
        "query": "What is Retrieval Augmented Generation?"
    }

    first = client.post("/chat", json=payload)

    second = client.post("/chat", json=payload)

    assert first.status_code == 200

    assert second.status_code == 200

    assert first.json()["answer"] == second.json()["answer"]