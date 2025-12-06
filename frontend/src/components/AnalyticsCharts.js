import React from 'react';
import { BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

function AnalyticsCharts({ analytics, reviews }) {
  // Prepare rating distribution data
  const ratingData = [
    { rating: '1★', count: parseInt(analytics.rating_distribution['1'] || 0) },
    { rating: '2★', count: parseInt(analytics.rating_distribution['2'] || 0) },
    { rating: '3★', count: parseInt(analytics.rating_distribution['3'] || 0) },
    { rating: '4★', count: parseInt(analytics.rating_distribution['4'] || 0) },
    { rating: '5★', count: parseInt(analytics.rating_distribution['5'] || 0) },
  ];

  // Prepare trend data (last 10 reviews)
  const trendData = reviews.slice(-10).map((review, index) => ({
    index: index + 1,
    rating: review.rating,
  }));

  return (
    <div className="grid grid-2 mt-4">
      <div className="card">
        <div className="card-header">Rating Distribution</div>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={ratingData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#000" />
            <XAxis dataKey="rating" stroke="#000" style={{ fontWeight: 600 }} />
            <YAxis stroke="#000" style={{ fontWeight: 600 }} />
            <Tooltip 
              contentStyle={{ 
                border: '3px solid #000', 
                borderRadius: '0',
                backgroundColor: '#FFF',
                fontWeight: 600
              }}
            />
            <Bar dataKey="count" fill="#FFD93D" stroke="#000" strokeWidth={2} />
          </BarChart>
        </ResponsiveContainer>
      </div>

      <div className="card">
        <div className="card-header">Rating Trend (Last 10)</div>
        <ResponsiveContainer width="100%" height={300}>
          <LineChart data={trendData}>
            <CartesianGrid strokeDasharray="3 3" stroke="#000" />
            <XAxis dataKey="index" stroke="#000" style={{ fontWeight: 600 }} />
            <YAxis domain={[0, 6]} stroke="#000" style={{ fontWeight: 600 }} />
            <Tooltip 
              contentStyle={{ 
                border: '3px solid #000', 
                borderRadius: '0',
                backgroundColor: '#FFF',
                fontWeight: 600
              }}
            />
            <Line 
              type="monotone" 
              dataKey="rating" 
              stroke="#FF6B9D" 
              strokeWidth={3}
              dot={{ fill: '#FF6B9D', stroke: '#000', strokeWidth: 2, r: 6 }}
            />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default AnalyticsCharts;
