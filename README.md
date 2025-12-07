# 🚀 Fynd AI Intern - Take Home Assessment

**Submitted by:** Rahul  
**Email:** rahulchauhan4708@gmail.com  
**Date:** December 7, 2025

[![User Dashboard](https://img.shields.io/badge/User_Dashboard-Live-brightgreen)](https://ai-feedback-system.netlify.app/)
[![Admin Dashboard](https://img.shields.io/badge/Admin_Dashboard-Live-blue)](https://ai-feedback-system.netlify.app/admin)
[![Backend API](https://img.shields.io/badge/Backend_API-Live-orange)](https://fynd-ai-backend.onrender.com/docs)

---

## 📋 Overview

This repository contains my complete submission for the Fynd AI Intern Take Home Assessment, featuring:

1. **Task 1**: Rating Prediction via Prompting (Jupyter Notebook)
2. **Task 2**: AI-Powered Feedback System with User & Admin Dashboards (Full-Stack Web App)

**Completion Time:** ~12 hours  
**Tech Stack:** FastAPI, React, Google Gemini 2.5 Flash API, Pandas, Recharts

---

## 🌐 Live Deployments

### 🎯 **Try the Live Applications:**

| Dashboard | URL | Description |
|-----------|-----|-------------|
| **User Dashboard** | [ai-feedback-system.netlify.app](https://ai-feedback-system.netlify.app/) | Submit reviews and get AI responses |
| **Admin Dashboard** | [ai-feedback-system.netlify.app/admin](https://ai-feedback-system.netlify.app/admin) | View analytics, manage reviews, generate AI insights |
| **Backend API** | [fynd-ai-backend.onrender.com](https://fynd-ai-backend.onrender.com) | RESTful API server |
| **API Docs** | [fynd-ai-backend.onrender.com/docs](https://fynd-ai-backend.onrender.com/docs) | Interactive Swagger documentation |

---

## 📁 Repository Structure

```
fynd-ai-assessment/
├── 📓 task1_rating_prediction.ipynb    # Task 1: Jupyter Notebook
├── 📊 task1_results/                   # Task 1: Evaluation results
│   ├── results_zero_shot.csv
│   ├── results_few_shot.csv
│   ├── results_chain_of_thought.csv
│   ├── all_results_combined.csv
│   ├── metrics_comparison.csv
│   └── task1_summary.json
├── 🔧 backend/                         # Task 2: FastAPI Backend
│   ├── app/
│   │   ├── api/                        # API endpoints
│   │   ├── models/                     # Pydantic schemas
│   │   └── services/                   # Business logic & AI
│   ├── requirements.txt
│   └── render.yaml                     # Render deployment config
├── 🎨 frontend/                        # Task 2: React Frontend
│   ├── src/
│   │   ├── components/                 # Reusable components
│   │   ├── pages/                      # User & Admin dashboards
│   │   ├── services/                   # API client
│   │   └── styles/                     # Neubrutalism CSS
│   ├── package.json
│   └── netlify.toml                    # Netlify deployment config
├── 📚 docs/                            # Additional documentation
│   ├── API_DOCUMENTATION.md
│   ├── DEPLOYMENT.md
│   └── QUICKSTART.md
├── 📄 SUBMISSION_REPORT.md             # Comprehensive report
├── 📖 README.md                        # This file
├── .gitignore
├── requirements.txt                    # Python dependencies
└── yelp.csv                            # Yelp dataset
```

---

## 🎯 Task 1: Rating Prediction via Prompting

### 📊 Results Summary

Implemented and evaluated **3 prompting approaches** on 200 Yelp reviews:

| Approach | Exact Accuracy | Within-1 Accuracy | MAE | RMSE | JSON Validity |
|----------|---------------|-------------------|-----|------|---------------|
| **Zero-Shot** | 45.5% | 78.5% | 0.67 | 0.89 | 98.0% |
| **Few-Shot** ⭐ | **52.0%** | **85.0%** | **0.54** | **0.72** | **99.5%** |
| **Chain-of-Thought** | 49.5% | 83.0% | 0.59 | 0.78 | 97.5% |

**Winner:** Few-Shot Prompting (best accuracy-cost balance)

### 🔍 Key Insights

- **Few-Shot outperformed** by providing concrete examples for rating calibration
- **Chain-of-Thought** showed strong reasoning but sometimes over-analyzed simple reviews
- **JSON validity** consistently >97% across all approaches with proper prompt engineering
- Common challenges: 4 vs 5-star differentiation, mixed-sentiment reviews

### 📓 Notebook

**File:** [`task1_rating_prediction.ipynb`](task1_rating_prediction.ipynb)

**Contents:**
- Dataset loading and sampling (200 reviews)
- Implementation of all 3 prompting approaches
- Comprehensive evaluation metrics
- Visualizations and comparison tables
- Prompt iteration documentation

---

## 🌐 Task 2: AI Feedback System

### 🏗️ Architecture

```
┌─────────────────────┐
│   Frontend (React)  │
│  Netlify CDN        │  ← User & Admin Dashboards
└──────────┬──────────┘
           │ HTTPS/REST
           ▼
┌─────────────────────┐
│  Backend (FastAPI)  │
│  Render.com         │  ← API Server
└──────────┬──────────┘
           │
           ├─────► CSV Storage
           └─────► Gemini 2.5 Flash API
```

### ✨ Features

#### 👤 User Dashboard
- ⭐ Interactive 1-5 star rating selector
- ✍️ Review text input with real-time feedback
- 🤖 AI-generated personalized responses
- 🎨 Bold Neubrutalism design (custom CSS)

#### 👨‍💼 Admin Dashboard
- 📊 Real-time metrics (total reviews, avg rating, sentiment breakdown)
- 📈 Interactive charts (rating distribution, trend analysis)
- 📋 Complete review list with filtering & sorting
- 🧠 On-demand AI insights (summary + recommended actions)
- 🎨 Sentiment-based color coding (green/yellow/red)

### 🛠️ Tech Stack

**Backend:**
- FastAPI (Python 3.13) - High-performance async API
- Google Gemini 2.5 Flash - AI integration
- Pandas - Data processing
- Pydantic - Schema validation
- Uvicorn - ASGI server

**Frontend:**
- React 18.2 - UI library
- React Router 6 - Client-side routing
- Recharts - Data visualization
- Axios - HTTP client
- Custom Neubrutalism CSS - Bold modern design

**Deployment:**
- Netlify - Frontend CDN hosting
- Render - Backend API hosting
- GitHub - Version control

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Google Gemini API key

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Rahul4112002/fynd-ai-assessment.git
cd fynd-ai-assessment
```

### 2️⃣ Backend Setup
```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo GEMINI_API_KEY=your_api_key_here > .env

# Run backend
cd backend
uvicorn app.main:app --reload
```

Backend will run at: http://localhost:8000

### 3️⃣ Frontend Setup
```bash
# In a new terminal
cd frontend

# Install dependencies
npm install

# Run frontend
npm start
```

Frontend will run at: http://localhost:3000

### 4️⃣ Access Dashboards
- **User Dashboard:** http://localhost:3000/
- **Admin Dashboard:** http://localhost:3000/admin
- **API Docs:** http://localhost:8000/docs

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [SUBMISSION_REPORT.md](SUBMISSION_REPORT.md) | Comprehensive report covering both tasks, design decisions, evaluation, and learnings |
| [docs/API_DOCUMENTATION.md](docs/API_DOCUMENTATION.md) | Complete API reference with endpoints and schemas |
| [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) | Deployment guides for Netlify and Render |
| [docs/QUICKSTART.md](docs/QUICKSTART.md) | 5-minute setup guide |

---

## 🎨 Design Highlights

### Neubrutalism UI
- **Bold Borders:** 3px solid black outlines
- **Brutal Shadows:** 4px offset for depth
- **Vibrant Colors:** Yellow (#FFD93D), Green (#6BCF7F), Pink (#FF6B9D)
- **Sharp Corners:** No border radius
- **High Contrast:** Excellent accessibility
- **Space Grotesk Font:** Modern geometric typeface

### UX Decisions
- **Lazy-loaded AI insights** - Reduces API costs, faster initial load
- **Sentiment color coding** - Quick visual feedback for admins
- **Real-time metrics** - Immediate data visibility
- **Responsive design** - Works on all screen sizes

---

## 🔍 Evaluation & Learnings

### Task 1 Learnings
✅ Few-shot prompting beats complex reasoning for structured tasks  
✅ Explicit JSON schemas dramatically improve validity (60% → 99%)  
✅ Prompt iteration is 80% of accuracy improvements  
✅ Multiple metrics reveal different performance aspects  

### Task 2 Learnings
✅ FastAPI + React = clean separation of concerns  
✅ CSV sufficient for MVP, plan migration path early  
✅ Graceful error handling improves trust  
✅ Bold design creates memorable experiences  

---

## 📦 Deliverables

- ✅ GitHub Repository (this repo)
- ✅ Task 1 Jupyter Notebook
- ✅ Task 2 Full-Stack Application
- ✅ User Dashboard (deployed)
- ✅ Admin Dashboard (deployed)
- ✅ Backend API (deployed)
- ✅ Comprehensive Documentation
- ✅ Evaluation Results & Comparison Tables

---

## 🚀 Future Enhancements

### Potential Improvements
- [ ] Real-time updates via WebSockets
- [ ] PostgreSQL migration for scalability
- [ ] Email notifications for admin
- [ ] Export analytics (PDF/CSV)
- [ ] Multi-language support
- [ ] A/B testing for AI responses
- [ ] Ensemble approach combining multiple prompts
- [ ] Confidence scores for predictions

---

## 🤝 Contact

**Rahul**  
📧 Email: rahulchauhan4708@gmail.com  
🔗 GitHub: [@Rahul4112002](https://github.com/Rahul4112002)

---

## 📄 License

This project was created as part of the Fynd AI Intern assessment.

---

**⭐ If you're evaluating this project, please check out the [live dashboards](https://ai-feedback-system.netlify.app/) and [comprehensive report](SUBMISSION_REPORT.md)!**
