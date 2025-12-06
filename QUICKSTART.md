# ⚡ Quick Start Guide - FastAPI + React

Get the Fynd AI Assessment running in **5 minutes**!

## 🚀 Prerequisites Check

```cmd
:: Check Python
python --version
:: Should show: Python 3.10+ 

:: Check Node.js
node --version
:: Should show: v16+

:: Check npm
npm --version
:: Should show: 8+
```

Don't have them? Install:
- **Python**: https://www.python.org/downloads/
- **Node.js**: https://nodejs.org/

---

## 🎯 One-Command Setup

```cmd
setup.bat
```

That's it! This installs everything you need.

---

## 🏃 Run the Application

### Method 1: Using Batch Files (Recommended)

**Open TWO terminals:**

**Terminal 1 - Backend:**
```cmd
run_backend.bat
```
✅ Backend running at http://localhost:8000

**Terminal 2 - Frontend:**
```cmd
run_frontend.bat
```
✅ Frontend running at http://localhost:3000

### Method 2: Manual Commands

**Terminal 1 - Backend:**
```cmd
.venv\Scripts\activate
cd backend
python -m uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```cmd
cd frontend
npm start
```

---

## 🌐 Access Points

| Service | URL | Description |
|---------|-----|-------------|
| **Frontend (User)** | http://localhost:3000 | Submit reviews |
| **Frontend (Admin)** | http://localhost:3000/admin | View analytics |
| **Backend API** | http://localhost:8000 | API server |
| **API Docs** | http://localhost:8000/docs | Swagger UI |
| **API ReDoc** | http://localhost:8000/redoc | Alternative docs |

---

## 📊 Quick Workflow

### 1. Submit a Review (User Page)

1. Go to http://localhost:3000
2. Select star rating (1-5)
3. Write review text
4. Click **Submit Review**
5. Get AI-generated personalized response

### 2. View Analytics (Admin Page)

1. Go to http://localhost:3000/admin
2. See metrics:
   - Total Reviews
   - Average Rating
   - Sentiment Breakdown
   - Recent Activity
3. View charts:
   - Rating Distribution
   - Rating Trend
4. Filter and sort reviews
5. Generate AI insights for reviews

### 3. Use Task 1 Notebook

```cmd
.venv\Scripts\activate
jupyter notebook task1_rating_prediction.ipynb
```

Test three prompting approaches:
- Zero-Shot
- Few-Shot
- Chain-of-Thought

---

## 🧪 Test the API

### Using Browser

Visit http://localhost:8000/docs and try:
1. `POST /api/reviews/submit` - Submit review
2. `GET /api/reviews/all` - Get all reviews
3. `GET /api/reviews/analytics` - Get metrics

### Using curl

**Submit Review:**
```cmd
curl -X POST http://localhost:8000/api/reviews/submit ^
  -H "Content-Type: application/json" ^
  -d "{\"business_id\":\"test123\",\"review_text\":\"Amazing experience!\",\"stars\":5,\"user_id\":\"user1\"}"
```

**Get All Reviews:**
```cmd
curl http://localhost:8000/api/reviews/all
```

**Get Analytics:**
```cmd
curl http://localhost:8000/api/reviews/analytics
```

**Predict Rating (Zero-Shot):**
```cmd
curl -X POST http://localhost:8000/api/predictions/predict/zero-shot ^
  -H "Content-Type: application/json" ^
  -d "{\"review_text\":\"The food was delicious and service was excellent!\"}"
```

---

## 🎨 Features to Try

### User Page
✨ Interactive star rating
✨ Real-time text input
✨ AI-generated responses
✨ Beautiful Neubrutalism design

### Admin Dashboard
📊 Real-time metrics
📈 Interactive charts
🔍 Filter by rating
🔄 Sort reviews
💡 AI-generated insights
📝 Review summaries
🎯 Recommended actions

---

## 🐛 Quick Troubleshooting

### Backend Won't Start

**Port already in use:**
```cmd
:: Find process on port 8000
netstat -ano | findstr :8000

:: Kill process (replace PID)
taskkill /PID <PID> /F

:: Or use different port
uvicorn app.main:app --port 8001
```

**Module not found:**
```cmd
:: Activate environment
.venv\Scripts\activate

:: Reinstall dependencies
cd backend
pip install -r requirements.txt
```

### Frontend Won't Start

**Port 3000 busy:**
```
:: Kill process or choose different port when prompted
```

**Dependencies missing:**
```cmd
cd frontend
npm install
```

**Build errors:**
```cmd
:: Clear cache
npm cache clean --force

:: Delete and reinstall
rmdir /s /q node_modules
del package-lock.json
npm install
```

### CORS Errors

1. Verify backend is running
2. Check `backend/app/main.py` CORS settings
3. Ensure frontend API URL is correct in `frontend/src/services/api.js`

### AI Responses Not Working

1. Check `.env` file has `GEMINI_API_KEY`
2. Verify API key is valid
3. Check backend logs for errors

---

## 📁 Project Structure Quick Reference

```
fynd-ai-assessment/
├── backend/               # FastAPI Backend
│   ├── app/
│   │   ├── api/          # Endpoints
│   │   ├── models/       # Data models
│   │   ├── services/     # Business logic
│   │   └── main.py       # FastAPI app
│   └── data/             # CSV storage
│
├── frontend/             # React Frontend
│   ├── src/
│   │   ├── components/   # React components
│   │   ├── pages/        # User & Admin pages
│   │   ├── services/     # API client
│   │   └── styles/       # Neubrutalism CSS
│   └── public/
│
├── task1_rating_prediction.ipynb  # Jupyter Notebook
├── yelp.csv              # Dataset
├── .env                  # Environment variables
├── setup.bat             # Setup script
├── run_backend.bat       # Run backend
└── run_frontend.bat      # Run frontend
```

---

## 💡 Common Tasks

### Add New Review Manually
```cmd
:: Via curl
curl -X POST http://localhost:8000/api/reviews/submit ^
  -H "Content-Type: application/json" ^
  -d "{\"business_id\":\"biz1\",\"review_text\":\"Great!\",\"stars\":5,\"user_id\":\"user1\"}"
```

### Clear All Reviews
```cmd
:: Delete submissions file
del backend\data\submissions.csv
```

### View Data File
```cmd
:: Open in Excel or text editor
notepad backend\data\submissions.csv
```

### Restart Services
```cmd
:: Backend: Press Ctrl+C, then run again
run_backend.bat

:: Frontend: Press Ctrl+C, then run again
run_frontend.bat
```

---

## 🚀 Next Steps

1. ✅ **Run locally** - Complete above steps
2. ✅ **Test features** - Try User and Admin pages
3. ✅ **Explore API** - Check /docs endpoint
4. ✅ **Run notebook** - Complete Task 1
5. ✅ **Deploy** - See [DEPLOYMENT.md](DEPLOYMENT.md)
6. ✅ **Customize** - Modify code as needed

---

## 📚 Learn More

- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **React Docs**: https://react.dev/
- **Gemini API**: https://ai.google.dev/docs
- **Neubrutalism Design**: https://hype4.academy/tools/neubrutalism-generator

---

## 🎯 Assessment Checklist

### Task 1: Rating Prediction
- [ ] Open `task1_rating_prediction.ipynb`
- [ ] Run all cells
- [ ] Review three approaches
- [ ] Check evaluation metrics
- [ ] Export results

### Task 2: Web Application
- [ ] User page works
- [ ] Admin dashboard displays data
- [ ] AI responses generate
- [ ] Charts render correctly
- [ ] Filtering/sorting works

### Deployment
- [ ] Backend deployed
- [ ] Frontend deployed
- [ ] Both URLs public
- [ ] End-to-end test passes

### Documentation
- [ ] README.md updated
- [ ] REPORT.md created
- [ ] Code commented
- [ ] Repository clean

---

## ⚡ Speed Run (Already Know What You're Doing?)

```cmd
:: 1. Setup
setup.bat

:: 2. Run (Terminal 1)
run_backend.bat

:: 3. Run (Terminal 2)
run_frontend.bat

:: 4. Open
start http://localhost:3000
```

**Done! 🎉**

---

## 🆘 Getting Help

**Check these in order:**
1. Error message in terminal
2. Browser console (F12)
3. Backend logs (terminal running backend)
4. API docs at /docs
5. README.md troubleshooting section
6. DEPLOYMENT.md for production issues

**Still stuck?**
- Check `.env` file exists
- Verify Python/Node versions
- Ensure ports 8000 and 3000 are free
- Try restarting both services

---

**Happy Coding! 🚀**

*Built with FastAPI + React + Gemini AI*
