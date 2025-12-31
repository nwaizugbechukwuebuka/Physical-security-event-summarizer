import logging

class EmailIngestor:
    def ingest(self, email_data):
        logging.info("Ingesting incident from email.")
        # Parse and return incident data from email
        return {"source": "email", "details": email_data}
