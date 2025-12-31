def format_incident(incident: dict) -> str:
    return f"[{incident.get('timestamp')}] {incident.get('source')}: {incident.get('details')}"
