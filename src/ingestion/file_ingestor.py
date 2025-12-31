import logging

class FileIngestor:
    def ingest(self, file_path):
        logging.info(f"Ingesting incident from file: {file_path}")
        # Read and return incident data from file
        return {"source": "file", "details": f"Data from {file_path}"}
