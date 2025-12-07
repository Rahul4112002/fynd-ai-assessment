# Fynd AI Intern - Take Home Assessment Report

**Submitted by:** Rahul  
**Email:** rahulchauhan4708@gmail.com  
**Date:** December 7, 2025  
**Completion Time:** ~12 hours

---

## 📋 Executive Summary

This report documents the completion of the Fynd AI Intern Take Home Assessment, consisting of two main tasks:
1. **Task 1**: Rating Prediction via Prompting (Jupyter Notebook)
2. **Task 2**: Two-Dashboard AI Feedback System (Web Application)

Both tasks leverage Google Gemini 2.5 Flash API for AI-powered features and are deployed with public URLs.

---

## 🎯 Task 1: Rating Prediction via Prompting

### Dataset
- **Source**: Yelp Reviews Dataset (Kaggle)
- **Sample Size**: 200 reviews (stratified sampling to maintain rating distribution)
- **Distribution**: Balanced across 1-5 star ratings

### Prompting Approaches Implemented

#### 1. Zero-Shot Prompting

**Design Decision:**  
Direct classification without examples, relying on the model's pre-trained understanding of sentiment and rating scales.

**Prompt Structure:**
```
You are a review rating classifier. Analyze the following Yelp review 
and predict the star rating (1-5 stars).

Review: "{review_text}"

Return your response as a JSON object with:
{
  "predicted_stars": <number between 1-5>,
  "explanation": "<brief reasoning>"
}
```

**Rationale:**
- Simplest approach - baseline for comparison
- Fast execution with minimal token usage
- Tests model's inherent capabilities

**Advantages:**
- ✅ Fastest inference time
- ✅ Lowest API cost
- ✅ Simple implementation

**Disadvantages:**
- ❌ No contextual examples
- ❌ May misinterpret edge cases

---

#### 2. Few-Shot Prompting

**Design Decision:**  
Provide 5 example reviews (one per star rating) to guide the model's understanding of rating nuances.

**Prompt Structure:**
```
You are a review rating classifier. Based on these examples, 
predict the star rating (1-5) for the given review.

EXAMPLES:

Review: "Absolutely terrible experience..."
Output: {"predicted_stars": 1, "explanation": "..."}

Review: "Not impressed. The food was mediocre..."
Output: {"predicted_stars": 2, "explanation": "..."}

[... 3 more examples for 3, 4, 5 stars ...]

NOW CLASSIFY THIS REVIEW:
Review: "{review_text}"
```

**Rationale:**
- Provides clear examples of each rating level
- Helps model understand rating calibration
- Balances accuracy with efficiency

**Advantages:**
- ✅ Better context understanding
- ✅ Improved rating calibration
- ✅ Higher accuracy than zero-shot

**Disadvantages:**
- ❌ Longer prompts (higher token cost)
- ❌ Examples may bias predictions

---

#### 3. Chain-of-Thought Prompting

**Design Decision:**  
Encourage step-by-step reasoning before prediction to improve accuracy on complex reviews.

**Prompt Structure:**
```
You are a review rating classifier. Analyze the review step-by-step:

Review: "{review_text}"

Think through this systematically:
1. Identify overall sentiment (positive/negative/neutral)
2. Note specific positive aspects mentioned
3. Note specific negative aspects mentioned
4. Consider intensity of language used
5. Determine if there's intent to return/recommend
6. Based on these factors, predict the star rating

Return JSON:
{
  "predicted_stars": <1-5>,
  "explanation": "<reasoning covering key factors>"
}
```

**Rationale:**
- Forces deliberate analysis of review components
- Reduces impulsive predictions
- Better handling of mixed-sentiment reviews

**Advantages:**
- ✅ Most thorough reasoning
- ✅ Better for complex reviews
- ✅ Explainable predictions

**Disadvantages:**
- ❌ Slowest inference time
- ❌ Highest token consumption
- ❌ May over-analyze simple reviews

---

### Evaluation Metrics

All approaches were evaluated on 200 reviews using:

1. **Exact Accuracy (%)**: Percentage of predictions matching actual rating exactly
2. **Within-1 Accuracy (%)**: Predictions within ±1 star of actual (e.g., predicting 4 for actual 5)
3. **JSON Validity (%)**: Successfully parsed JSON responses
4. **Mean Absolute Error (MAE)**: Average absolute difference between predicted and actual
5. **Root Mean Squared Error (RMSE)**: Penalizes larger errors more heavily

### Results Comparison

| Approach | Exact Accuracy | Within-1 Accuracy | JSON Validity | MAE | RMSE |
|----------|---------------|-------------------|---------------|-----|------|
| Zero-Shot | 45.5% | 78.5% | 98.0% | 0.67 | 0.89 |
| Few-Shot | 52.0% | 85.0% | 99.5% | 0.54 | 0.72 |
| Chain-of-Thought | 49.5% | 83.0% | 97.5% | 0.59 | 0.78 |

### Key Findings

#### Best Performing Approach: **Few-Shot Prompting**

**Why Few-Shot Won:**
- ✅ Highest exact accuracy (52.0%)
- ✅ Best within-1 accuracy (85.0%)
- ✅ Lowest error metrics (MAE: 0.54)
- ✅ Excellent JSON validity (99.5%)
- ✅ Good balance of speed and accuracy

**Insights:**

1. **Few-Shot superiority**: Examples helped the model calibrate rating scales better than reasoning alone
2. **Chain-of-Thought trade-offs**: While theoretically better, CoT sometimes over-analyzed simple reviews
3. **Zero-Shot baseline**: Surprisingly strong performance given no examples
4. **JSON Reliability**: All approaches achieved >97% JSON validity with proper prompt engineering

**Common Error Patterns:**

- **4-star vs 5-star confusion**: Model often predicted 4 stars for enthusiastic 5-star reviews
- **2-star vs 3-star boundary**: Neutral language sometimes misclassified
- **Mixed sentiment**: Reviews with both praise and criticism were challenging

**Prompt Iteration Process:**

1. **Initial attempts**: Generic prompts resulted in ~30% accuracy
2. **Added JSON schema**: Improved validity from 60% to 95%
3. **Refined examples**: Choosing diverse, clear examples boosted few-shot to 52%
4. **Explicit reasoning steps**: Enhanced CoT performance but not enough to beat few-shot

### Recommendations

**For Production Use:**
- **Use Few-Shot** for best accuracy-cost balance
- **Use Zero-Shot** for high-volume, cost-sensitive applications
- **Use Chain-of-Thought** for critical predictions requiring explainability

---

## 🌐 Task 2: Two-Dashboard AI Feedback System

### Architecture Overview

**Tech Stack:**
- **Backend**: FastAPI (Python) - RESTful API
- **Frontend**: React 18.2 - Single Page Application
- **AI**: Google Gemini 2.5 Flash API
- **Database**: CSV-based persistence (lightweight)
- **Styling**: Custom Neubrutalism CSS (bold, modern design)
- **Package Management**: UV (Python), npm (Node.js)

**Design Philosophy:**
Modern client-server architecture with clear separation of concerns, RESTful API design, and bold visual design for engagement.

---

### A. User Dashboard (Public-Facing)

**URL**: https://ai-feedback-system.netlify.app/

**Features Implemented:**

1. **Interactive Star Rating Selector**
   - Visual 1-5 star selection
   - Hover effects for engagement
   - Immediate visual feedback

2. **Review Text Input**
   - Large textarea for user reviews
   - Real-time character feedback
   - Placeholder text guidance

3. **AI-Powered Response**
   - Personalized thank-you messages
   - Sentiment-aware responses
   - Different tones for different ratings:
     - 1-3 stars: Apologetic, improvement-focused
     - 4-5 stars: Appreciative, encouraging return

4. **Neubrutalism Design**
   - Bold 3px black borders
   - Vibrant colors (yellow, green, pink)
   - Brutal shadows for depth
   - Space Grotesk font
   - No border radius (sharp corners)

**User Flow:**
```
1. User visits dashboard
2. Selects star rating (1-5)
3. Writes review text
4. Clicks "Submit Review"
5. Backend processes:
   - Stores review in CSV
   - Generates AI response via Gemini
6. User sees personalized AI response
7. Success confirmation
```

**API Integration:**
```javascript
// Submit review
POST /api/reviews/submit
{
  "business_id": "string",
  "user_id": "string",
  "review_text": "string",
  "stars": 1-5
}

Response:
{
  "message": "Success",
  "ai_response": "Personalized message",
  "review_id": "unique_id"
}
```

---

### B. Admin Dashboard (Internal-Facing)

**URL**: https://ai-feedback-system.netlify.app/admin

**Features Implemented:**

1. **Real-Time Metrics (Top Cards)**
   - Total Reviews Count
   - Average Rating (calculated)
   - Positive/Neutral/Negative breakdown
   - Latest review timestamp

2. **Interactive Analytics Charts**
   - **Rating Distribution**: Bar chart showing 1-5 star counts
   - **Rating Trend**: Line chart of last 10 reviews
   - Built with Recharts library
   - Responsive and interactive

3. **Review Management**
   - Complete list of all submissions
   - Star rating display (visual stars)
   - Customer review text
   - AI-generated response
   - Timestamp for each review

4. **AI Insights Generation** (On-Demand)
   - **Summary**: One-sentence review summary
   - **Recommended Actions**: 2-3 specific action items
   - Lazy-loaded (click to generate)
   - Caching to avoid regeneration

5. **Filtering & Sorting**
   - Filter by star rating (1-5)
   - Sort by:
     - Newest first
     - Oldest first
     - Highest rating
     - Lowest rating

6. **Sentiment-Based Visual Coding**
   - Green border: 4-5 stars (positive)
   - Yellow border: 3 stars (neutral)
   - Red border: 1-2 stars (negative)

**Admin Flow:**
```
1. Admin visits dashboard
2. Views real-time metrics
3. Sees analytics charts
4. Scrolls through review list
5. Clicks "Generate AI Insights" on specific review
6. Backend generates:
   - AI summary of review
   - Recommended business actions
7. Insights display immediately
8. Can filter/sort for analysis
```

**API Endpoints Used:**

```javascript
// Get all reviews
GET /api/reviews/all
Response: { "reviews": [...] }

// Get analytics
GET /api/reviews/analytics
Response: {
  "total_reviews": 150,
  "average_rating": 4.2,
  "rating_distribution": {...},
  "recent_reviews": [...]
}

// Generate AI insights
POST /api/reviews/{id}/enrich
Response: {
  "ai_summary": "...",
  "recommended_actions": "..."
}
```

---

### AI Integration Details

**1. User Response Generation**
```python
Prompt: "You are a customer service rep. Generate a personalized 
response to this {rating}-star review: '{review_text}'"

Output: Warm, empathetic 2-3 sentence response
```

**2. Review Summarization**
```python
Prompt: "Provide a brief 1-sentence summary of this review: 
'{review_text}'"

Output: Concise summary highlighting key point
```

**3. Recommended Actions**
```python
Prompt: "Based on this {rating}-star review, suggest 2-3 specific, 
actionable next steps for the business: '{review_text}'"

Output: Bullet-point list of concrete actions
```

**API Configuration:**
- Model: Gemini 2.5 Flash
- Temperature: Default (balanced creativity/accuracy)
- Max Tokens: Sufficient for 200-word responses
- Error Handling: Fallback messages if API fails

---

### Data Storage Design

**Format**: CSV file (`backend/data/submissions.csv`)

**Schema:**
```
timestamp,rating,review,ai_response,ai_summary,recommended_actions
2025-12-06 12:53:23,5,"Amazing!","Thank you...","","
```

**Why CSV?**
- ✅ Lightweight (no DB setup required)
- ✅ Human-readable for debugging
- ✅ Easy to export/analyze
- ✅ Version-controllable
- ✅ Fast for <10,000 records

**Future Scalability:**
For production, migrate to:
- PostgreSQL (relational data)
- MongoDB (document-based)
- Firebase (real-time sync)

---

### Design Decisions

#### 1. Neubrutalism UI Choice

**Why Neubrutalism?**
- Stands out from typical corporate dashboards
- Bold, memorable visual identity
- Accessible (high contrast)
- Modern, trending design style
- Playful yet professional

**Implementation:**
- Custom CSS (no heavy UI frameworks)
- CSS variables for theming
- Responsive grid system
- Accessible color contrasts

#### 2. Client-Server Separation

**Why FastAPI + React?**
- Clear separation of concerns
- Independent scaling
- API can serve multiple frontends
- Modern development experience
- Type safety (Pydantic + PropTypes)

#### 3. Lazy-Loading AI Insights

**Why On-Demand?**
- Reduces initial API calls
- Lower cost (only when needed)
- Faster dashboard load time
- Admin controls when to generate

#### 4. CSV vs Database

**Why CSV for MVP?**
- No infrastructure overhead
- Simple deployment
- Easy debugging
- Sufficient for demo/assessment

---

### System Behavior & Error Handling

**Robust Error Handling:**

1. **Network Failures**: Toast notifications, retry logic
2. **AI API Errors**: Fallback messages, graceful degradation
3. **Invalid JSON**: Schema validation, default values
4. **NaN Values**: Data cleaning with pandas fillna()
5. **CORS Issues**: Middleware configuration

**Performance Optimizations:**

1. **Frontend**:
   - Component lazy loading
   - Memoization for charts
   - Debounced search/filter
   - Optimized re-renders

2. **Backend**:
   - Async/await for non-blocking I/O
   - Efficient pandas operations
   - Response streaming for large data

**Security Considerations:**

1. API key stored in .env (not in code)
2. CORS restrictions (specific origins)
3. Input validation (Pydantic models)
4. Rate limiting (future enhancement)

---

## 📊 Deployment Architecture

```
┌─────────────────────┐
│   Frontend (React)  │
│  Netlify CDN        │  ← User Dashboard & Admin Dashboard
│  Port 3000 (dev)    │
└──────────┬──────────┘
           │ HTTPS
           │ Axios API Calls
           ▼
┌─────────────────────┐
│  Backend (FastAPI)  │
│  Render.com         │  ← RESTful API Server
│  Port 8000          │
└──────────┬──────────┘
           │
           ├─────► CSV Storage (submissions.csv)
           │
           └─────► Gemini API (AI Features)
```

---

## 🎓 Key Learnings

### Technical Learnings

1. **Prompt Engineering**: Few-shot often beats complex reasoning
2. **JSON Reliability**: Explicit schema + examples = 99%+ validity
3. **API Design**: RESTful endpoints with clear responsibilities
4. **React State**: Managing async AI responses smoothly
5. **Error Handling**: Graceful degradation improves UX

### Design Learnings

1. **User Flow**: Simple, guided experiences drive engagement
2. **Visual Hierarchy**: Bold design helps focus attention
3. **Lazy Loading**: On-demand AI reduces cost and load time
4. **Feedback**: Immediate visual responses build trust

### Process Learnings

1. **Iteration**: Prompt refinement is 80% of accuracy gains
2. **Evaluation**: Multiple metrics reveal different aspects
3. **Documentation**: Clear explanations help future maintenance

---

## 🚀 Future Enhancements

### Task 1 Improvements
- [ ] Test GPT-4, Claude for comparison
- [ ] Implement ensemble voting (combine approaches)
- [ ] Add confidence scores to predictions
- [ ] Domain-specific fine-tuning

### Task 2 Enhancements
- [ ] Real-time updates (WebSockets)
- [ ] Email notifications to admin
- [ ] Export analytics (PDF/CSV)
- [ ] Multi-language support
- [ ] A/B testing for AI responses
- [ ] Sentiment analysis visualization
- [ ] PostgreSQL migration for scale

---

## 📦 Deliverables Checklist

- [x] GitHub Repository with all code
- [x] Task 1 Jupyter Notebook (task1_rating_prediction.ipynb)
- [x] Task 2 Application Code (FastAPI + React)
- [x] Deployment Links (Frontend + Backend)
- [x] User Dashboard (deployed)
- [x] Admin Dashboard (deployed)
- [x] Comprehensive Report (this document)
- [x] README with setup instructions
- [x] API Documentation
- [x] Evaluation results and comparison tables

---

## 📝 Conclusion

This assessment successfully demonstrated:

1. ✅ **Prompt Engineering Skills**: Designed and evaluated 3 distinct approaches
2. ✅ **Full-Stack Development**: Built complete web application with modern stack
3. ✅ **AI Integration**: Leveraged Gemini API effectively for multiple use cases
4. ✅ **System Design**: Clean architecture with clear separation of concerns
5. ✅ **Deployment**: Both dashboards accessible via public URLs
6. ✅ **Documentation**: Comprehensive reporting of approach and findings

**Completion Time**: Approximately 12 hours (efficient iteration and deployment)

The project is production-ready for MVP deployment and demonstrates scalability considerations for future growth.

---

## 🔗 Deployment Links

- **GitHub Repository**: https://github.com/Rahul4112002/fynd-ai-assessment
- **User Dashboard**: https://ai-feedback-system.netlify.app/
- **Admin Dashboard**: https://ai-feedback-system.netlify.app/admin
- **Backend API**: https://fynd-ai-backend.onrender.com
- **API Documentation**: https://fynd-ai-backend.onrender.com/docs

---

**Thank you for the opportunity!**
