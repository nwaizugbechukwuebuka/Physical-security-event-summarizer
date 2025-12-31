from fastapi import APIRouter
from .schemas import Incident, SummaryResponse

api_router = APIRouter()

@api_router.post("/summarize", response_model=SummaryResponse)
def summarize_event(incident: Incident):
    # Placeholder for event summarization logic
    return SummaryResponse(summary="Event summary placeholder.")
