from fastapi import APIRouter
from app.services.feedback_logger import log_feedback

from app.models.schemas import (
    ConversationRequest,
    ConversationResponse,
    EventAnalysisRequest,
    EventAnalysisResponse,
    FactCheckRequest,
    FactCheckResponse,
)

from app.services.event_analyzer import analyze_event
from app.services.topic_generator import generate_topics
from app.services.fact_checker import fact_check
from app.services.history_logger import log_conversation

router = APIRouter()


@router.post(
    "/analyze-event",
    response_model=EventAnalysisResponse
)
def analyze_event_endpoint(request: EventAnalysisRequest):
    themes = analyze_event(request.description)

    return {
        "themes": themes
    }
    return EventAnalysisResponse(
        themes=themes
    )


@router.post(
    "/fact-check",
    response_model=FactCheckResponse
)
def check_fact(request: FactCheckRequest):
    result = fact_check(request.query)

    return FactCheckResponse(
        result=result
    )


@router.post(
    "/generate-conversation",
    response_model=ConversationResponse
)
def generate_conversation(request: ConversationRequest):

    themes = analyze_event(request.description)

    suggestions = generate_topics(
        themes,
        request.interests
    )

    log_conversation(
        {
            "description": request.description,
            "interests": request.interests,
            "themes": themes,
            "suggestions": suggestions,
        }
    )

    return ConversationResponse(
        themes=themes,
        suggestions=suggestions
    )
@router.post("/feedback")
def feedback(request: dict):

    log_feedback(
    request["suggestion"],
    request["action"]
)

    return {
        "message": "Feedback saved successfully"
    }