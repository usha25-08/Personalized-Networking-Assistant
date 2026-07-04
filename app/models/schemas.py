from pydantic import BaseModel
from typing import List


class ConversationRequest(BaseModel):
    description: str
    interests: List[str]


class ConversationResponse(BaseModel):
    themes: List[str]
    suggestions: List[str]


class EventAnalysisRequest(BaseModel):
    description: str


class EventAnalysisResponse(BaseModel):
    themes: List[str]


class FactCheckRequest(BaseModel):
    query: str


class FactCheckResponse(BaseModel):
    result: str