from fastapi import APIRouter, HTTPException
from app.models.schemas import ReviewSubmission, ReviewResponse, AnalyticsResponse
from app.services.ai_service import AIService
from app.services.data_service import DataService

router = APIRouter()

@router.post("/submit", response_model=ReviewResponse)
async def submit_review(submission: ReviewSubmission):
    """Submit a new review"""
    try:
        # Generate AI response
        ai_response = await AIService.generate_user_response(
            submission.rating, 
            submission.review
        )
        
        # Save submission
        result = await DataService.save_submission(
            rating=submission.rating,
            review=submission.review,
            ai_response=ai_response
        )
        
        return ReviewResponse(**result)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/all")
async def get_all_reviews():
    """Get all review submissions"""
    try:
        reviews = await DataService.get_all_submissions()
        return {"reviews": reviews}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/analytics", response_model=AnalyticsResponse)
async def get_analytics():
    """Get analytics data"""
    try:
        analytics = await DataService.get_analytics()
        return analytics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/{review_id}/enrich")
async def enrich_review(review_id: int):
    """Enrich a review with AI summary and recommendations"""
    try:
        reviews = await DataService.get_all_submissions()
        
        if review_id < 0 or review_id >= len(reviews):
            raise HTTPException(status_code=404, detail="Review not found")
        
        review = reviews[review_id]
        
        # Generate AI insights if not already present
        if not review.get('ai_summary'):
            print(f"Enriching review {review_id}: {review['review'][:50]}...")
            ai_summary = await AIService.generate_summary(review['review'])
            recommended_actions = await AIService.generate_recommended_actions(
                review['rating'], 
                review['review']
            )
            
            print(f"Enrichment complete. Summary: {ai_summary}")
            
            # Update would require modifying the CSV - for simplicity, return enriched data
            return {
                **review,
                'ai_summary': ai_summary,
                'recommended_actions': recommended_actions
            }
        
        return review
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error in enrich_review: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
