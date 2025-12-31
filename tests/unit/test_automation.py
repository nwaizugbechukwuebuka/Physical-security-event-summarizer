from src.automation.n8n_client import N8NClient
import pytest
import requests
from unittest.mock import patch

def test_trigger_workflow():
    client = N8NClient(base_url="http://localhost:5678", api_key="test")
    with patch.object(requests, "post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": "success"}
        response = client.trigger_workflow("workflow_id", {"data": 123})
        assert response["result"] == "success"
