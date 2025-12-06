from fastapi import APIRouter, HTTPException
from app.models.schemas import PredictionRequest, PredictionResponse
from app.services.ai_service import AIService

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
async def predict_rating(request: PredictionRequest):
    """Predict star rating from review text"""
    try:
        result = await AIService.predict_rating(
            request.review_text,
            request.approach
        )
        
        return PredictionResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict/zero-shot", response_model=PredictionResponse)
async def predict_zero_shot(review_text: str):
    """Predict using zero-shot approach"""
    result = await AIService.predict_rating(review_text, "zero-shot")
    return PredictionResponse(**result)

@router.post("/predict/few-shot", response_model=PredictionResponse)
async def predict_few_shot(review_text: str):
    """Predict using few-shot approach"""
    result = await AIService.predict_rating(review_text, "few-shot")
    return PredictionResponse(**result)

@router.post("/predict/chain-of-thought", response_model=PredictionResponse)
async def predict_chain_of_thought(review_text: str):
    """Predict using chain-of-thought approach"""
    result = await AIService.predict_rating(review_text, "chain-of-thought")
    return PredictionResponse(**result)
