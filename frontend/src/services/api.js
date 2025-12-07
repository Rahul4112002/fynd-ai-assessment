import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://fynd-ai-backend.onrender.com/api';

export const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Review endpoints
export const reviewsAPI = {
  submit: (data) => api.post('/reviews/submit', data),
  getAll: () => api.get('/reviews/all'),
  getAnalytics: () => api.get('/reviews/analytics'),
  enrichReview: (reviewId) => api.post(`/reviews/${reviewId}/enrich`),
};

// Prediction endpoints
export const predictionsAPI = {
  predict: (data) => api.post('/predictions/predict', data),
  predictZeroShot: (reviewText) => 
    api.post('/predictions/predict/zero-shot', null, { params: { review_text: reviewText } }),
  predictFewShot: (reviewText) => 
    api.post('/predictions/predict/few-shot', null, { params: { review_text: reviewText } }),
  predictChainOfThought: (reviewText) => 
    api.post('/predictions/predict/chain-of-thought', null, { params: { review_text: reviewText } }),
};

export default api;
