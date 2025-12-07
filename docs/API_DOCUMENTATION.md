# 📖 API Documentation - Fynd AI Assessment

Complete API reference for the FastAPI backend.

## 🌐 Base URLs

- **Development**: http://localhost:8000
- **Production**: https://your-backend-url.com

## 📚 Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔌 Endpoints Overview

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/api/reviews/submit` | POST | Submit new review |
| `/api/reviews/all` | GET | Get all reviews |
| `/api/reviews/analytics` | GET | Get analytics data |
| `/api/reviews/{review_id}/enrich` | POST | Generate AI insights |
| `/api/predictions/predict` | POST | Predict rating (any approach) |
| `/api/predictions/predict/zero-shot` | POST | Zero-shot prediction |
| `/api/predictions/predict/few-shot` | POST | Few-shot prediction |
| `/api/predictions/predict/chain-of-thought` | POST | CoT prediction |

---

## 🏥 Health Check

### `GET /health`

Check if the API is running.

**Response:**
```json
{
  "status": "healthy"
}
```

**Status Codes:**
- `200 OK` - Service is healthy

**Example:**
```bash
curl http://localhost:8000/health
```

---

## 📝 Reviews API

### Submit Review

`POST /api/reviews/submit`

Submit a new customer review.

**Request Body:**
```json
{
  "business_id": "string",
  "user_id": "string",
  "review_text": "string",
  "stars": 1-5
}
```

**Parameters:**
- `business_id` (required, string): Unique business identifier
- `user_id` (required, string): User identifier
- `review_text` (required, string): Review content
- `stars` (required, integer): Rating 1-5

**Response:**
```json
{
  "message": "Review submitted successfully",
  "ai_response": "Thank you for your 5-star review! We're thrilled...",
  "review_id": "unique_id_timestamp"
}
```

**Status Codes:**
- `200 OK` - Review submitted successfully
- `422 Unprocessable Entity` - Validation error
- `500 Internal Server Error` - Server error

**Example:**
```bash
curl -X POST http://localhost:8000/api/reviews/submit \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "cafe_123",
    "user_id": "user_456",
    "review_text": "Amazing coffee and friendly staff!",
    "stars": 5
  }'
```

---

### Get All Reviews

`GET /api/reviews/all`

Retrieve all submitted reviews.

**Response:**
```json
{
  "reviews": [
    {
      "review_id": "cafe_123_user_456_1234567890",
      "business_id": "cafe_123",
      "user_id": "user_456",
      "review_text": "Amazing coffee and friendly staff!",
      "stars": 5,
      "ai_response": "Thank you for your wonderful feedback!",
      "timestamp": "2024-01-15T10:30:00",
      "sentiment": "positive"
    }
  ]
}
```

**Status Codes:**
- `200 OK` - Reviews retrieved successfully
- `500 Internal Server Error` - Server error

**Example:**
```bash
curl http://localhost:8000/api/reviews/all
```

---

### Get Analytics

`GET /api/reviews/analytics`

Get aggregated analytics data.

**Response:**
```json
{
  "total_reviews": 150,
  "average_rating": 4.2,
  "rating_distribution": {
    "1": 5,
    "2": 10,
    "3": 25,
    "4": 50,
    "5": 60
  },
  "sentiment_breakdown": {
    "positive": 110,
    "neutral": 25,
    "negative": 15
  },
  "recent_reviews": [
    {
      "review_id": "...",
      "stars": 5,
      "review_text": "...",
      "timestamp": "..."
    }
  ]
}
```

**Status Codes:**
- `200 OK` - Analytics retrieved successfully
- `500 Internal Server Error` - Server error

**Example:**
```bash
curl http://localhost:8000/api/reviews/analytics
```

---

### Enrich Review

`POST /api/reviews/{review_id}/enrich`

Generate AI insights for a specific review.

**Path Parameters:**
- `review_id` (required): Unique review identifier

**Response:**
```json
{
  "review_id": "cafe_123_user_456_1234567890",
  "summary": "Customer praised coffee quality and staff friendliness",
  "recommended_actions": [
    "Maintain high coffee quality standards",
    "Continue staff training programs",
    "Consider loyalty program for repeat customers"
  ],
  "insights": {
    "sentiment": "positive",
    "key_topics": ["coffee", "staff", "service"],
    "urgency": "low"
  }
}
```

**Status Codes:**
- `200 OK` - Insights generated successfully
- `404 Not Found` - Review not found
- `500 Internal Server Error` - Server error

**Example:**
```bash
curl -X POST http://localhost:8000/api/reviews/cafe_123_user_456_1234567890/enrich
```

---

## 🎯 Predictions API

### Predict Rating (Flexible)

`POST /api/predictions/predict`

Predict rating using specified approach.

**Request Body:**
```json
{
  "review_text": "string",
  "approach": "zero-shot" | "few-shot" | "chain-of-thought"
}
```

**Parameters:**
- `review_text` (required, string): Review text to analyze
- `approach` (optional, string): Prediction approach (default: "zero-shot")

**Response:**
```json
{
  "predicted_rating": 4,
  "confidence": 0.85,
  "approach_used": "zero-shot",
  "reasoning": "The review expresses positive sentiment..."
}
```

**Status Codes:**
- `200 OK` - Prediction successful
- `422 Unprocessable Entity` - Invalid approach
- `500 Internal Server Error` - Server error

**Example:**
```bash
curl -X POST http://localhost:8000/api/predictions/predict \
  -H "Content-Type: application/json" \
  -d '{
    "review_text": "The food was good but service was slow",
    "approach": "chain-of-thought"
  }'
```

---

### Zero-Shot Prediction

`POST /api/predictions/predict/zero-shot`

Predict rating using zero-shot prompting.

**Request Body:**
```json
{
  "review_text": "string"
}
```

**Response:**
```json
{
  "predicted_rating": 3,
  "confidence": 0.75,
  "approach": "zero-shot",
  "explanation": "Direct classification based on sentiment"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/predictions/predict/zero-shot \
  -H "Content-Type: application/json" \
  -d '{
    "review_text": "Decent experience, nothing special"
  }'
```

---

### Few-Shot Prediction

`POST /api/predictions/predict/few-shot`

Predict rating using few-shot prompting with examples.

**Request Body:**
```json
{
  "review_text": "string"
}
```

**Response:**
```json
{
  "predicted_rating": 4,
  "confidence": 0.88,
  "approach": "few-shot",
  "matched_examples": [
    "Similar to: 'Great service and food' -> 5 stars"
  ]
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/predictions/predict/few-shot \
  -H "Content-Type: application/json" \
  -d '{
    "review_text": "Excellent food and ambiance!"
  }'
```

---

### Chain-of-Thought Prediction

`POST /api/predictions/predict/chain-of-thought`

Predict rating using chain-of-thought reasoning.

**Request Body:**
```json
{
  "review_text": "string"
}
```

**Response:**
```json
{
  "predicted_rating": 2,
  "confidence": 0.82,
  "approach": "chain-of-thought",
  "reasoning_steps": [
    "Step 1: Identify key aspects mentioned",
    "Step 2: Analyze sentiment for each aspect",
    "Step 3: Weigh importance of aspects",
    "Step 4: Determine overall rating"
  ],
  "aspect_analysis": {
    "food": "negative",
    "service": "neutral",
    "ambiance": "positive"
  }
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/api/predictions/predict/chain-of-thought \
  -H "Content-Type: application/json" \
  -d '{
    "review_text": "Food was terrible but nice decor"
  }'
```

---

## 📊 Data Models

### ReviewSubmission

```typescript
{
  business_id: string;      // Unique business identifier
  user_id: string;          // User identifier
  review_text: string;      // Review content
  stars: 1 | 2 | 3 | 4 | 5; // Rating
}
```

### ReviewResponse

```typescript
{
  message: string;          // Success message
  ai_response: string;      // Personalized AI response
  review_id: string;        // Generated review ID
}
```

### Review (Full)

```typescript
{
  review_id: string;        // Unique identifier
  business_id: string;      // Business ID
  user_id: string;          // User ID
  review_text: string;      // Review content
  stars: number;            // Rating 1-5
  ai_response: string;      // AI-generated response
  timestamp: string;        // ISO 8601 datetime
  sentiment: string;        // positive/neutral/negative
  summary?: string;         // AI-generated summary
  recommended_actions?: string[]; // AI recommendations
}
```

### Analytics

```typescript
{
  total_reviews: number;
  average_rating: number;
  rating_distribution: {
    "1": number;
    "2": number;
    "3": number;
    "4": number;
    "5": number;
  };
  sentiment_breakdown: {
    positive: number;
    neutral: number;
    negative: number;
  };
  recent_reviews: Review[];
}
```

### PredictionRequest

```typescript
{
  review_text: string;      // Text to analyze
  approach?: string;        // "zero-shot" | "few-shot" | "chain-of-thought"
}
```

### PredictionResponse

```typescript
{
  predicted_rating: number; // 1-5
  confidence: number;       // 0-1
  approach: string;         // Approach used
  reasoning?: string;       // Explanation
  reasoning_steps?: string[]; // CoT steps
  aspect_analysis?: object; // Aspect sentiments
}
```

---

## 🔒 Error Handling

### Standard Error Response

```json
{
  "detail": "Error message description"
}
```

### Common Error Codes

| Code | Meaning | Common Cause |
|------|---------|--------------|
| 400 | Bad Request | Invalid JSON format |
| 404 | Not Found | Review ID doesn't exist |
| 422 | Unprocessable Entity | Validation error (missing fields, invalid values) |
| 500 | Internal Server Error | Server/AI service error |

### Validation Errors

**Example:**
```json
{
  "detail": [
    {
      "loc": ["body", "stars"],
      "msg": "ensure this value is greater than or equal to 1",
      "type": "value_error.number.not_ge"
    }
  ]
}
```

---

## 🚀 Rate Limiting

Currently no rate limiting implemented. For production:

**Recommended limits:**
- Reviews submission: 10 per minute per IP
- Analytics: 60 per minute
- Predictions: 30 per minute
- Enrich: 20 per minute

---

## 🔐 Authentication

Currently no authentication required (development mode).

For production, implement:
- API key authentication
- JWT tokens
- OAuth 2.0

**Example with API Key:**
```bash
curl http://localhost:8000/api/reviews/all \
  -H "X-API-Key: your_api_key_here"
```

---

## 📝 Request/Response Examples

### Complete Review Submission Flow

```bash
# 1. Submit review
curl -X POST http://localhost:8000/api/reviews/submit \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "rest_001",
    "user_id": "user_123",
    "review_text": "Best pizza in town!",
    "stars": 5
  }'

# Response:
# {
#   "message": "Review submitted successfully",
#   "ai_response": "Thank you for your 5-star review! We're delighted...",
#   "review_id": "rest_001_user_123_1705318800"
# }

# 2. Enrich with AI insights
curl -X POST http://localhost:8000/api/reviews/rest_001_user_123_1705318800/enrich

# Response:
# {
#   "review_id": "rest_001_user_123_1705318800",
#   "summary": "Customer highly satisfied with pizza quality",
#   "recommended_actions": [...]
# }

# 3. Get analytics
curl http://localhost:8000/api/reviews/analytics

# Response:
# {
#   "total_reviews": 1,
#   "average_rating": 5.0,
#   ...
# }
```

---

## 🧪 Testing with Postman

### Import Collection

Create collection with these endpoints:

1. **Health Check**
   - GET http://localhost:8000/health

2. **Submit Review**
   - POST http://localhost:8000/api/reviews/submit
   - Body: Raw JSON

3. **Get Reviews**
   - GET http://localhost:8000/api/reviews/all

4. **Analytics**
   - GET http://localhost:8000/api/reviews/analytics

5. **Predict Rating**
   - POST http://localhost:8000/api/predictions/predict
   - Body: Raw JSON

---

## 📖 OpenAPI Specification

Full OpenAPI 3.0 spec available at:
- JSON: http://localhost:8000/openapi.json
- Interactive: http://localhost:8000/docs

---

## 💡 Best Practices

### Request Format
- Always use JSON content type
- Include all required fields
- Validate data client-side first

### Error Handling
- Check HTTP status codes
- Parse error messages
- Implement retry logic for 5xx errors

### Performance
- Cache analytics responses
- Batch review submissions if possible
- Use pagination for large datasets

### Security
- Sanitize user input
- Validate review_text length
- Rate limit requests

---

## 🔄 Versioning

Current version: **v1**

Future versions will use URL path:
- v1: /api/v1/reviews/...
- v2: /api/v2/reviews/...

---

## 📞 Support

For API issues:
1. Check this documentation
2. Visit /docs for interactive testing
3. Review error messages
4. Check server logs

---

**API Documentation Complete! 📚**

*Powered by FastAPI + Google Gemini AI*
