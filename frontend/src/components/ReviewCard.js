import React, { useState } from 'react';
import { reviewsAPI } from '../services/api';

function ReviewCard({ review, reviewId }) {
  const [enriched, setEnriched] = useState(false);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState(review.ai_summary || '');
  const [actions, setActions] = useState(review.recommended_actions || '');

  const getSentimentClass = (rating) => {
    if (rating <= 2) return 'danger';
    if (rating === 3) return 'warning';
    return 'success';
  };

  const handleEnrich = async () => {
    if (enriched || (summary && actions)) return;
    
    setLoading(true);
    try {
      const result = await reviewsAPI.enrichReview(reviewId);
      setSummary(result.data.ai_summary);
      setActions(result.data.recommended_actions);
      setEnriched(true);
    } catch (err) {
      console.error('Failed to enrich review:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card mb-3 animate-slide-in" style={{
      borderLeft: `8px solid var(--color-${getSentimentClass(review.rating)})`
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
        <div>
          <div style={{ fontSize: '1.5rem' }}>
            {'⭐'.repeat(review.rating)}
          </div>
          <div className="font-semibold">
            {review.rating} / 5 Stars
          </div>
        </div>
        <div style={{ textAlign: 'right', opacity: 0.7 }}>
          {review.timestamp}
        </div>
      </div>

      <div className="grid grid-2" style={{ gap: '24px' }}>
        <div>
          <div className="font-bold mb-2">Customer Review:</div>
          <div style={{ 
            backgroundColor: 'var(--color-bg)', 
            padding: '12px', 
            border: '2px solid var(--color-black)',
            marginBottom: '16px'
          }}>
            {review.review}
          </div>

          {(summary || loading) && (
            <div>
              <div className="font-bold mb-2">AI Summary:</div>
              {loading ? (
                <div className="spinner" style={{ width: '20px', height: '20px' }}></div>
              ) : (
                <div className={`alert alert-info`}>
                  {summary}
                </div>
              )}
            </div>
          )}
        </div>

        <div>
          <div className="font-bold mb-2">Our Response:</div>
          <div style={{ 
            backgroundColor: 'var(--color-bg)', 
            padding: '12px', 
            border: '2px solid var(--color-black)',
            marginBottom: '16px'
          }}>
            {review.ai_response}
          </div>

          {(actions || loading) && (
            <div>
              <div className="font-bold mb-2">Recommended Actions:</div>
              {loading ? (
                <div className="spinner" style={{ width: '20px', height: '20px' }}></div>
              ) : (
                <div className="alert alert-success" style={{ whiteSpace: 'pre-line' }}>
                  {actions}
                </div>
              )}
            </div>
          )}

          {!summary && !actions && !loading && (
            <button 
              className="btn btn-primary btn-small" 
              onClick={handleEnrich}
            >
              🤖 Generate AI Insights
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default ReviewCard;
