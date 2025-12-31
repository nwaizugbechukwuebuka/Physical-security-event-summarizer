from pydantic import BaseModel

class Incident(BaseModel):
    timestamp: str
    source: str
    details: str

class SummaryResponse(BaseModel):
    summary: str
