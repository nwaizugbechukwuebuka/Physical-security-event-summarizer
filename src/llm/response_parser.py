def parse_response(response: dict) -> str:
    # Extract summary from LLM response
    return response.get("summary", "No summary available.")
