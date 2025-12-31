import logging

class WebhookIngestor:
    def ingest(self, webhook_payload):
        logging.info("Ingesting incident from webhook.")
        # Parse and return incident data from webhook
        return {"source": "webhook", "details": webhook_payload}
