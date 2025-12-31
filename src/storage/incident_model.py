from pydantic import BaseModel

class IncidentModel(BaseModel):
    id: str
    timestamp: str
    type: str
    description: str
    severity: str
