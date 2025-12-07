from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import reviews, predictions
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="Fynd AI Assessment API",
    description="Rating Prediction & Feedback System API",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://ai-feedback-system.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(reviews.router, prefix="/api/reviews", tags=["reviews"])
app.include_router(predictions.router, prefix="/api/predictions", tags=["predictions"])

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Fynd AI Assessment API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
