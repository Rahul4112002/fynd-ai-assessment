import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash')

class AIService:
    """Service for AI-powered features using Gemini"""
    
    @staticmethod
    async def generate_user_response(rating: int, review: str) -> str:
        """Generate personalized response to user review"""
        prompt = f"""You are a friendly customer service representative. A customer has left a {rating}-star review.

Review: "{review}"

Generate a personalized, empathetic response that:
1. Thanks the customer for their feedback
2. Acknowledges their specific experience
3. For ratings 1-3: Apologizes and shows commitment to improvement
4. For ratings 4-5: Expresses appreciation and encouragement to return

Keep the response warm, professional, and concise (2-3 sentences).
"""
        
        try:
            response = model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Thank you for your {rating}-star review! We appreciate your feedback and will use it to improve our service."
    
    @staticmethod
    async def generate_summary(review: str) -> str:
        """Generate brief summary of review"""
        prompt = f"""Provide a brief 1-sentence summary of this customer review, highlighting the key point:

Review: "{review}"

Summary:"""
        
        try:
            print(f"Generating summary for review: {review[:50]}...")
            response = model.generate_content(prompt)
            summary = response.text.strip()
            print(f"Generated summary: {summary}")
            return summary
        except Exception as e:
            print(f"Error generating summary: {str(e)}")
            import traceback
            traceback.print_exc()
            # Return a meaningful fallback
            return f"Customer feedback about their experience"
    
    @staticmethod
    async def generate_recommended_actions(rating: int, review: str) -> str:
        """Generate recommended actions based on review"""
        prompt = f"""Based on this {rating}-star customer review, suggest 2-3 specific, actionable next steps for the business:

Review: "{review}"

Provide concrete actions the business should take. Be specific and practical.
Format your response EXACTLY like this:
• First action point
• Second action point
• Third action point

Keep each point concise (1-2 sentences max)."""
        
        try:
            print(f"Generating actions for {rating}-star review...")
            response = model.generate_content(prompt)
            actions = response.text.strip()
            print(f"Generated actions: {actions[:100]}...")
            return actions
        except Exception as e:
            print(f"Error generating actions: {str(e)}")
            import traceback
            traceback.print_exc()
            return "• Follow up with customer\n• Review internal processes\n• Implement improvements based on feedback"
    
    @staticmethod
    async def predict_rating(review_text: str, approach: str = "few-shot") -> dict:
        """Predict star rating from review text"""
        
        if approach == "zero-shot":
            prompt = AIService._zero_shot_prompt(review_text)
        elif approach == "few-shot":
            prompt = AIService._few_shot_prompt(review_text)
        else:  # chain-of-thought
            prompt = AIService._chain_of_thought_prompt(review_text)
        
        try:
            response = model.generate_content(prompt)
            response_text = response.text.strip()
            
            # Extract JSON
            if '```json' in response_text:
                response_text = response_text.split('```json')[1].split('```')[0].strip()
            elif '```' in response_text:
                response_text = response_text.split('```')[1].split('```')[0].strip()
            
            # Parse JSON
            result = json.loads(response_text)
            
            # Validate
            if 'predicted_stars' in result and 'explanation' in result:
                result['predicted_stars'] = int(result['predicted_stars'])
                if 1 <= result['predicted_stars'] <= 5:
                    result['json_valid'] = True
                    result['approach_used'] = approach
                    return result
            
            return {
                'predicted_stars': 3,
                'explanation': 'Could not parse prediction',
                'json_valid': False,
                'approach_used': approach
            }
            
        except Exception as e:
            return {
                'predicted_stars': 3,
                'explanation': f'Error: {str(e)}',
                'json_valid': False,
                'approach_used': approach
            }
    
    @staticmethod
    def _zero_shot_prompt(review_text: str) -> str:
        """Zero-shot prompting approach"""
        return f"""You are a review rating classifier. Analyze the following Yelp review and predict the star rating (1-5 stars).

Review: "{review_text}"

Return your response as a JSON object with this exact format:
{{
  "predicted_stars": <number between 1-5>,
  "explanation": "<brief reasoning for the assigned rating>"
}}

Only return the JSON object, nothing else."""
    
    @staticmethod
    def _few_shot_prompt(review_text: str) -> str:
        """Few-shot prompting approach"""
        return f"""You are a review rating classifier. Based on the examples below, predict the star rating (1-5) for the given review.

EXAMPLES:

Review: "Absolutely terrible experience. Food was cold, service was rude, and the place was dirty. Never coming back."
Output: {{"predicted_stars": 1, "explanation": "Extremely negative review mentioning multiple severe issues."}}

Review: "Not impressed. The food was mediocre and overpriced. Server seemed disinterested."
Output: {{"predicted_stars": 2, "explanation": "Predominantly negative with multiple complaints but not extremely hostile."}}

Review: "It was okay. Nothing special but nothing terrible either. Average food, average service."
Output: {{"predicted_stars": 3, "explanation": "Neutral review indicating average experience across the board."}}

Review: "Really enjoyed our meal! Good food, friendly staff, and nice atmosphere. Would come again."
Output: {{"predicted_stars": 4, "explanation": "Positive review with multiple compliments and intent to return."}}

Review: "Outstanding! Best meal I've had in years. Incredible service, amazing flavors, perfect ambiance. Absolutely phenomenal!"
Output: {{"predicted_stars": 5, "explanation": "Extremely positive with superlatives and enthusiasm throughout."}}

NOW CLASSIFY THIS REVIEW:
Review: "{review_text}"

Return only the JSON object with predicted_stars and explanation."""
    
    @staticmethod
    def _chain_of_thought_prompt(review_text: str) -> str:
        """Chain-of-thought prompting approach"""
        return f"""You are a review rating classifier. Analyze the following review step-by-step to predict its star rating (1-5).

Review: "{review_text}"

Think through this systematically:
1. Identify the overall sentiment (positive, negative, neutral)
2. Note specific positive aspects mentioned
3. Note specific negative aspects mentioned
4. Consider the intensity of language used
5. Determine if there's intent to return/recommend
6. Based on these factors, predict the star rating

Return your response as a JSON object:
{{
  "predicted_stars": <number between 1-5>,
  "explanation": "<concise reasoning covering the key factors that led to this rating>"
}}

Only return the JSON object."""
