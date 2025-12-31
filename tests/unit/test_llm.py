from src.llm.client import LLMClient
from src.llm.response_parser import parse_response
from src.llm.validator import validate_summary

def test_llm_client():
    client = LLMClient(api_key="test")
    summary = client.summarize("Test text.")
    assert "LLM summary" in summary

def test_parse_response():
    response = {"summary": "Test summary."}
    assert parse_response(response) == "Test summary."

def test_validate_summary():
    assert validate_summary("A valid summary string.")
    assert not validate_summary("")
