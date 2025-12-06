import pandas as pd
import os
from datetime import datetime
from typing import List, Dict

class DataService:
    """Service for data persistence and retrieval"""
    
    SUBMISSIONS_FILE = 'data/submissions.csv'
    
    @staticmethod
    def ensure_data_file():
        """Ensure data directory and file exist"""
        os.makedirs('data', exist_ok=True)
        if not os.path.exists(DataService.SUBMISSIONS_FILE):
            df = pd.DataFrame(columns=[
                'timestamp', 'rating', 'review', 'ai_response', 
                'ai_summary', 'recommended_actions'
            ])
            df.to_csv(DataService.SUBMISSIONS_FILE, index=False)
    
    @staticmethod
    async def save_submission(rating: int, review: str, ai_response: str,
                             ai_summary: str = None, recommended_actions: str = None) -> Dict:
        """Save a review submission"""
        DataService.ensure_data_file()
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        new_data = pd.DataFrame([{
            'timestamp': timestamp,
            'rating': rating,
            'review': review,
            'ai_response': ai_response,
            'ai_summary': ai_summary or '',
            'recommended_actions': recommended_actions or ''
        }])
        
        # Append to existing file
        df = pd.read_csv(DataService.SUBMISSIONS_FILE)
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_csv(DataService.SUBMISSIONS_FILE, index=False)
        
        return {
            'timestamp': timestamp,
            'rating': rating,
            'review': review,
            'ai_response': ai_response,
            'ai_summary': ai_summary,
            'recommended_actions': recommended_actions
        }
    
    @staticmethod
    async def get_all_submissions() -> List[Dict]:
        """Get all review submissions"""
        DataService.ensure_data_file()
        
        df = pd.read_csv(DataService.SUBMISSIONS_FILE)
        # Replace NaN with None for JSON serialization
        df = df.fillna('')
        return df.to_dict('records')
    
    @staticmethod
    async def get_analytics() -> Dict:
        """Get analytics data"""
        DataService.ensure_data_file()
        
        df = pd.read_csv(DataService.SUBMISSIONS_FILE)
        
        if len(df) == 0:
            return {
                'total_reviews': 0,
                'average_rating': 0,
                'rating_distribution': {},
                'recent_reviews': []
            }
        
        # Calculate metrics
        total_reviews = len(df)
        average_rating = df['rating'].mean()
        rating_distribution = df['rating'].value_counts().to_dict()
        
        # Get recent reviews (last 10)
        df_recent = df.tail(10).fillna('')
        recent_reviews = df_recent.to_dict('records')
        
        return {
            'total_reviews': int(total_reviews),
            'average_rating': float(round(average_rating, 2)),
            'rating_distribution': {str(int(k)): int(v) for k, v in rating_distribution.items()},
            'recent_reviews': recent_reviews
        }
