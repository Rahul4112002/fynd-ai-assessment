import React, { useState } from 'react';
import { reviewsAPI } from '../services/api';

function UserPage() {
  const [rating, setRating] = useState(5);
  const [review, setReview] = useState('');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!review.trim()) {
      setError('Please write a review before submitting');
      return;
    }

    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const result = await reviewsAPI.submit({ rating, review });
      setResponse(result.data);
      setReview('');
      setRating(5);
    } catch (err) {
      setError(err.response?.data?.detail || 'Failed to submit review');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <div style={{ maxWidth: '800px', margin: '40px auto' }}>
        <div className="card card-primary animate-slide-in">
          <div className="card-header">
            Share Your Experience
          </div>
          
          <div style={{ marginBottom: '24px' }}>
            <label className="font-bold mb-2" style={{ display: 'block' }}>
              Rate Your Experience
            </label>
            <div className="rating-selector">
              {[1, 2, 3, 4, 5].map((star) => (
                <button
                  key={star}
                  className={`star-btn ${rating >= star ? 'active' : ''}`}
                  onClick={() => setRating(star)}
                  type="button"
                >
                  {rating >= star ? '⭐' : '☆'}
                </button>
              ))}
            </div>
            <div className="mt-2 font-semibold">
              {rating} out of 5 stars
            </div>
          </div>

          <form onSubmit={handleSubmit}>
            <div style={{ marginBottom: '24px' }}>
              <label className="font-bold mb-2" style={{ display: 'block' }}>
                Your Review
              </label>
              <textarea
                className="input"
                value={review}
                onChange={(e) => setReview(e.target.value)}
                placeholder="Tell us about your experience..."
                rows="6"
              />
            </div>

            <button 
              type="submit" 
              className="btn btn-accent btn-large" 
              style={{ width: '100%' }}
              disabled={loading}
            >
              {loading ? 'Submitting...' : 'Submit Feedback'}
            </button>
          </form>

          {error && (
            <div className="alert alert-danger mt-3 animate-slide-in">
              {error}
            </div>
          )}

          {response && (
            <div className="card card-secondary mt-3 animate-slide-in">
              <div className="font-bold mb-2 text-xl">
                ✓ Thank You for Your Feedback!
              </div>
              <div className="font-semibold mb-1">Our Response:</div>
              <div style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>
                {response.ai_response}
              </div>
              <div className="mt-2" style={{ fontSize: '0.9rem', opacity: 0.8 }}>
                Submitted at: {response.timestamp}
              </div>
            </div>
          )}
        </div>

        <div className="card mt-4">
          <div className="text-center">
            <p className="font-semibold">
              Your feedback helps us improve our service
            </p>
            <p style={{ marginTop: '8px', opacity: 0.7 }}>
              Powered by AI | Fynd Assessment 2024
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UserPage;
