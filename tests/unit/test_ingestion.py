import pytest
from src.ingestion.email_ingestor import EmailIngestor
from src.ingestion.webhook_ingestor import WebhookIngestor
from src.ingestion.file_ingestor import FileIngestor

def test_email_ingestor():
    ingestor = EmailIngestor()
    result = ingestor.ingest("test email data")
    assert result["source"] == "email"

def test_webhook_ingestor():
    ingestor = WebhookIngestor()
    result = ingestor.ingest("test webhook data")
    assert result["source"] == "webhook"

def test_file_ingestor():
    ingestor = FileIngestor()
    result = ingestor.ingest("test_file.txt")
    assert result["source"] == "file"
