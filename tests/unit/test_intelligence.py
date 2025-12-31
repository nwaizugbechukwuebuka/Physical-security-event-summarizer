from src.intelligence.event_summarizer import EventSummarizer
from src.intelligence.incident_classifier import IncidentClassifier

def test_event_summarizer():
    summarizer = EventSummarizer()
    summary = summarizer.summarize("Test incident details.")
    assert "Summary of" in summary

def test_incident_classifier():
    classifier = IncidentClassifier()
    result = classifier.classify("Test incident details.")
    assert result == "classified_incident_type"
