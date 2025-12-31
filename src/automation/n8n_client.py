import logging
import requests

class N8NClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def trigger_workflow(self, workflow_id: str, data: dict):
        logging.info(f"Triggering n8n workflow {workflow_id}")
        url = f"{self.base_url}/webhook/{workflow_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
