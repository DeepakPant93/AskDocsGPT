import base64
import os
import sys

import pytest
from fastapi.testclient import TestClient

from ...src.core.config import settings
from ...src.schema.v1.schema import AnswerResponse

# Create a TestClient for testing FastAPI routes
client = None


# Define a fixture to mock the QAService dependency
@pytest.fixture
def mock_qa_service(monkeypatch):
    # Add the parent directory of 'src' to sys.path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
    from src.service.qa_service import QAService
    from main import app

    # Initialize the TestClient
    global client
    client = TestClient(app)

    async def mock_ask(self, question):
        return AnswerResponse(answer="This capital is Paris.")

    monkeypatch.setattr(QAService, "ask", mock_ask)
    yield


@pytest.fixture
def populate_auth_headers():
    # Define basic authentication credentials
    username = settings.BASIC_AUTH_USERNAME
    password = settings.BASIC_AUTH_PASSWORD

    # Encode the credentials in Base64 for Basic Auth
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("utf-8")

    # Define the headers with Authorization
    headers = {
        "Authorization": f"Basic {credentials}"
    }
    return headers


# Test case for the ask_question endpoint
def test_ask_question(mock_qa_service, populate_auth_headers):
    # Prepare request data
    question_request = {
        "question": "What is the capital of France?"
    }

    # Send a POST request to the /ask endpoint
    response = client.post("/api/v1/docs/ask", json=question_request, headers=populate_auth_headers)

    # Assert that the status code is 200 OK
    assert response.status_code == 200

    # Assert the response matches the mocked output
    response_data = response.json()
    assert response_data["answer"] == "This capital is Paris."
