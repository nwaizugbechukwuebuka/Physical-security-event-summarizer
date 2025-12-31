import pytest
from src.ingestion.email_ingestor import EmailIngestor
from src.preprocessing.text_cleaner import clean_text
from src.intelligence.event_summarizer import EventSummarizer
from src.intelligence.incident_classifier import IncidentClassifier
from src.storage.repository import IncidentRepository

def test_full_pipeline():
    # Ingest
    email_data = "Suspicious activity detected at main gate."
    incident = EmailIngestor().ingest(email_data)
    # Preprocess
    cleaned = clean_text(incident["details"])
    # Summarize
    summary = EventSummarizer().summarize(cleaned)
    # Classify
    incident_type = IncidentClassifier().classify(cleaned)
    # Store
    repo = IncidentRepository()
    assert repo.save({"summary": summary, "type": incident_type})
