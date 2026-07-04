import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
def test_root_endpoint():

    response = client.get("/")

    assert response.status_code == 200
def test_generate_conversation():

    payload = {
        "description": "AI for Sustainable Cities",
        "interests": ["Machine Learning", "Sustainability"]
    }

    response = client.post(
        "/generate-conversation",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "themes" in data
    assert "suggestions" in data
def test_fact_check():

    payload = {
        "query": "Artificial Intelligence"
    }

    response = client.post(
        "/fact-check",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "result" in data
def test_feedback():

    payload = {
        "suggestion": "AI can improve healthcare.",
        "action": "like"
    }

    response = client.post(
        "/feedback",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Feedback saved successfully"