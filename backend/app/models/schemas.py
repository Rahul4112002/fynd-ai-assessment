from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

class ReviewSubmission(BaseModel):
    """Model for user review submission"""
    rating: int = Field(..., ge=1, le=5, description="Star rating from 1 to 5")
    review: str = Field(..., min_length=1, max_length=5000, description="Review text")
    
    @validator('review')
    def review_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Review cannot be empty')
        return v.strip()

class ReviewResponse(BaseModel):
    """Model for review response"""
    timestamp: str
    rating: int
    review: str
    ai_response: str
    ai_summary: Optional[str] = None
    recommended_actions: Optional[str] = None

class PredictionRequest(BaseModel):
    """Model for rating prediction request"""
    review_text: str = Field(..., min_length=1, description="Review text to predict rating")
    approach: str = Field(default="few-shot", description="Prompting approach: zero-shot, few-shot, or chain-of-thought")
    
    @validator('approach')
    def validate_approach(cls, v):
        allowed = ['zero-shot', 'few-shot', 'chain-of-thought']
        if v not in allowed:
            raise ValueError(f'Approach must be one of: {", ".join(allowed)}')
        return v

class PredictionResponse(BaseModel):
    """Model for rating prediction response"""
    predicted_stars: int = Field(..., ge=1, le=5)
    explanation: str
    approach_used: str
    json_valid: bool = True

class AnalyticsResponse(BaseModel):
    """Model for analytics data"""
    total_reviews: int
    average_rating: float
    rating_distribution: dict
    recent_reviews: list
