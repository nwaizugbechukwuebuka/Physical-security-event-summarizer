from src.automation.n8n_client import N8NClient
import pytest
import requests
from unittest.mock import patch

def test_n8n_webhook():
    client = N8NClient(base_url="http://localhost:5678", api_key="test")
    with patch.object(requests, "post") as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"result": "webhook triggered"}
        response = client.trigger_workflow("webhook_id", {"incident": "test"})
        assert response["result"] == "webhook triggered"
