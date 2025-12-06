import React, { useState, useEffect } from 'react';
import { reviewsAPI } from '../services/api';
import ReviewCard from '../components/ReviewCard';
import AnalyticsCharts from '../components/AnalyticsCharts';

function AdminPage() {
  const [reviews, setReviews] = useState([]);
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState('all');
  const [sortBy, setSortBy] = useState('newest');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [reviewsRes, analyticsRes] = await Promise.all([
        reviewsAPI.getAll(),
        reviewsAPI.getAnalytics()
      ]);
      setReviews(reviewsRes.data.reviews);
      setAnalytics(analyticsRes.data);
    } catch (err) {
      console.error('Failed to fetch data:', err);
    } finally {
      setLoading(false);
    }
  };

  const filteredAndSortedReviews = () => {
    let filtered = [...reviews];
    
    // Apply filter
    if (filter !== 'all') {
      const rating = parseInt(filter);
      filtered = filtered.filter(r => r.rating === rating);
    }
    
    // Apply sort
    filtered.sort((a, b) => {
      if (sortBy === 'newest') {
        return new Date(b.timestamp) - new Date(a.timestamp);
      } else if (sortBy === 'oldest') {
        return new Date(a.timestamp) - new Date(b.timestamp);
      } else if (sortBy === 'highest') {
        return b.rating - a.rating;
      } else {
        return a.rating - b.rating;
      }
    });
    
    return filtered;
  };

  if (loading) {
    return (
      <div className="container">
        <div className="spinner"></div>
        <p className="text-center mt-2">Loading dashboard...</p>
      </div>
    );
  }

  return (
    <div className="container">
      <div style={{ padding: '40px 0' }}>
        <h1 className="text-3xl font-bold mb-4">📊 Admin Dashboard</h1>
        
        {/* Metrics */}
        {analytics && (
          <div className="grid grid-4 mb-4">
            <div className="metric-card">
              <div className="metric-value">{analytics.total_reviews}</div>
              <div className="metric-label">Total Reviews</div>
            </div>
            <div className="metric-card" style={{ backgroundColor: 'var(--color-primary)' }}>
              <div className="metric-value">{analytics.average_rating.toFixed(2)} ⭐</div>
              <div className="metric-label">Average Rating</div>
            </div>
            <div className="metric-card" style={{ backgroundColor: 'var(--color-secondary)' }}>
              <div className="metric-value">
                {analytics.total_reviews > 0 
                  ? Math.round((Object.entries(analytics.rating_distribution)
                      .filter(([k]) => parseInt(k) >= 4)
                      .reduce((sum, [, v]) => sum + v, 0) / analytics.total_reviews) * 100)
                  : 0}%
              </div>
              <div className="metric-label">Positive Reviews</div>
            </div>
            <div className="metric-card" style={{ backgroundColor: 'var(--color-info)' }}>
              <div className="metric-value">
                {reviews.length > 0 ? reviews[reviews.length - 1].rating : 0} ⭐
              </div>
              <div className="metric-label">Latest Rating</div>
            </div>
          </div>
        )}

        {/* Analytics Charts */}
        {analytics && <AnalyticsCharts analytics={analytics} reviews={reviews} />}

        {/* Controls */}
        <div className="card mt-4">
          <div style={{ display: 'flex', gap: '16px', alignItems: 'center', flexWrap: 'wrap' }}>
            <div style={{ flex: '1', minWidth: '200px' }}>
              <label className="font-bold mb-1" style={{ display: 'block' }}>
                Filter by Rating
              </label>
              <select 
                className="input" 
                value={filter} 
                onChange={(e) => setFilter(e.target.value)}
              >
                <option value="all">All Ratings</option>
                <option value="5">5 Stars</option>
                <option value="4">4 Stars</option>
                <option value="3">3 Stars</option>
                <option value="2">2 Stars</option>
                <option value="1">1 Star</option>
              </select>
            </div>
            
            <div style={{ flex: '1', minWidth: '200px' }}>
              <label className="font-bold mb-1" style={{ display: 'block' }}>
                Sort By
              </label>
              <select 
                className="input" 
                value={sortBy} 
                onChange={(e) => setSortBy(e.target.value)}
              >
                <option value="newest">Newest First</option>
                <option value="oldest">Oldest First</option>
                <option value="highest">Highest Rating</option>
                <option value="lowest">Lowest Rating</option>
              </select>
            </div>
            
            <div style={{ alignSelf: 'flex-end' }}>
              <button className="btn btn-info" onClick={fetchData}>
                🔄 Refresh Data
              </button>
            </div>
          </div>
        </div>

        {/* Reviews List */}
        <div className="mt-4">
          <h2 className="text-2xl font-bold mb-3">
            💬 Customer Reviews ({filteredAndSortedReviews().length})
          </h2>
          
          {filteredAndSortedReviews().length === 0 ? (
            <div className="card text-center">
              <p className="font-semibold">No reviews found matching your filters.</p>
            </div>
          ) : (
            filteredAndSortedReviews().map((review, index) => (
              <ReviewCard key={index} review={review} reviewId={index} />
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default AdminPage;
