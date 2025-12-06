# Fynd AI Intern Assessment - Modern Stack Edition

**FastAPI Backend + React Frontend with Neubrutalism UI**

## 🚀 Live Deployments

- **Frontend (User + Admin)**: [Deploy to Vercel/Netlify]
- **Backend API**: [Deploy to Render/Railway]
- **API Documentation**: [Your API URL]/docs

## 📁 Project Structure

```
fynd-ai-assessment/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API routes
│   │   │   ├── reviews.py     # Review endpoints
│   │   │   └── predictions.py # Prediction endpoints
│   │   ├── models/            # Pydantic models
│   │   │   └── schemas.py
│   │   ├── services/          # Business logic
│   │   │   ├── ai_service.py  # Gemini AI integration
│   │   │   └── data_service.py # Data persistence
│   │   └── main.py           # FastAPI app
│   └── data/                  # Data storage
│
├── frontend/                   # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/        # React components
│   │   │   ├── ReviewCard.js
│   │   │   └── AnalyticsCharts.js
│   │   ├── pages/            # Page components
│   │   │   ├── UserPage.js   # User feedback page
│   │   │   └── AdminPage.js  # Admin dashboard
│   │   ├── services/         # API clients
│   │   │   └── api.js
│   │   ├── styles/           # CSS files
│   │   │   └── neubrutalism.css # Neubrutalism theme
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── task1_rating_prediction.ipynb  # Task 1 Jupyter Notebook
├── yelp.csv                       # Dataset
├── .env                           # Environment variables
├── requirements.txt               # Python dependencies
├── pyproject.toml                 # UV configuration
├── setup.bat                      # Automated setup script
├── run_backend.bat                # Run FastAPI server
├── run_frontend.bat               # Run React dev server
└── README.md                      # This file
```

## ⚙️ Technology Stack

### Backend
- **FastAPI** - Modern, fast Python web framework
- **Uvicorn** - ASGI server
- **Pandas** - Data manipulation
- **Google Gemini API** - AI/LLM integration
- **Pydantic** - Data validation

### Frontend
- **React** - UI library
- **React Router** - Navigation
- **Axios** - HTTP client
- **Recharts** - Charts and visualizations
- **Neubrutalism CSS** - Bold, modern design system

### Package Management
- **UV** - Fast Python package manager
- **npm** - Node.js package manager

## 🛠️ Quick Setup

### Prerequisites
- Python 3.10+
- Node.js 16+
- UV package manager
- Gemini API key (already in .env)

### One-Command Setup

```cmd
setup.bat
```

This will:
1. Install UV
2. Create Python virtual environment
3. Install Python dependencies
4. Install Node.js dependencies
5. Create data directory
6. Verify .env file

## 🎯 Running the Application

### Option 1: Using Batch Files (Windows)

**Terminal 1 - Backend:**
```cmd
run_backend.bat
```

**Terminal 2 - Frontend:**
```cmd
run_frontend.bat
```

### Option 2: Manual Commands

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

### Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc

## 📊 Task 1: Rating Prediction (Jupyter Notebook)

```cmd
.venv\Scripts\activate
jupyter notebook task1_rating_prediction.ipynb
```

The notebook implements three prompting approaches:
1. **Zero-Shot** - Direct classification
2. **Few-Shot** - Example-guided classification  
3. **Chain-of-Thought** - Reasoning-based classification

## 🌐 Task 2: Web Application

### User Page (http://localhost:3000/)

Features:
- ⭐ Interactive star rating selector
- 📝 Review text input
- 🤖 AI-generated personalized responses
- 🎨 Neubrutalism UI design

### Admin Dashboard (http://localhost:3000/admin)

Features:
- 📊 Real-time analytics
- 📈 Interactive charts (rating distribution, trends)
- 💡 AI-generated review summaries
- 🎯 AI-recommended actions
- 🔍 Filtering and sorting
- 🔄 Auto-refresh capability

## 🎨 Neubrutalism Design System

The frontend uses a modern Neubrutalism design with:
- **Bold borders** (3px solid black)
- **Brutal shadows** (offset box-shadows)
- **Vibrant colors** (Yellow, Green, Pink, Cyan)
- **Space Grotesk font**
- **No border radius** (sharp corners)
- **Playful interactions**

### Color Palette
```css
--color-primary: #FFD93D    (Yellow)
--color-secondary: #6BCF7F  (Green)
--color-accent: #FF6B9D     (Pink)
--color-info: #6BCFFF       (Cyan)
```

## 🔌 API Endpoints

### Reviews
- `POST /api/reviews/submit` - Submit new review
- `GET /api/reviews/all` - Get all reviews
- `GET /api/reviews/analytics` - Get analytics data
- `POST /api/reviews/{id}/enrich` - Generate AI insights

### Predictions
- `POST /api/predictions/predict` - Predict rating (any approach)
- `POST /api/predictions/predict/zero-shot` - Zero-shot prediction
- `POST /api/predictions/predict/few-shot` - Few-shot prediction
- `POST /api/predictions/predict/chain-of-thought` - CoT prediction

Full API documentation: http://localhost:8000/docs

## 🚢 Deployment

### Backend (Render/Railway)

1. **Create account** on Render.com or Railway.app
2. **Connect GitHub** repository
3. **Select** `backend` folder as root
4. **Add environment variable**: `GEMINI_API_KEY`
5. **Build command**: `pip install -r requirements.txt`
6. **Start command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Vercel/Netlify)

1. **Create account** on Vercel or Netlify
2. **Connect GitHub** repository
3. **Select** `frontend` folder as root
4. **Build command**: `npm run build`
5. **Publish directory**: `build`
6. **Add environment variable**: `REACT_APP_API_URL=<your-backend-url>`

### Alternative: Full-Stack Deployment

**Using Docker Compose** (create docker-compose.yml):
```yaml
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
  
  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    environment:
      - REACT_APP_API_URL=http://backend:8000
```

## 🧪 Testing

### Backend
```cmd
cd backend
pytest
```

### Frontend
```cmd
cd frontend
npm test
```

### Manual Testing
1. Submit reviews via User page
2. View them in Admin dashboard
3. Generate AI insights
4. Check API responses in browser DevTools

## 📦 Building for Production

### Backend
```cmd
cd backend
pip install -r requirements.txt
```

### Frontend
```cmd
cd frontend
npm run build
```

Creates optimized production build in `frontend/build/`

## 🔐 Environment Variables

Create `.env` file in project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Frontend environment (`.env` in `frontend/`):
```env
REACT_APP_API_URL=http://localhost:8000/api
```

## 🐛 Troubleshooting

### Backend won't start
```cmd
# Check if port 8000 is in use
netstat -ano | findstr :8000

# Try different port
uvicorn app.main:app --port 8001
```

### Frontend won't start
```cmd
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rmdir /s frontend\node_modules
cd frontend
npm install
```

### CORS errors
- Ensure backend is running
- Check CORS configuration in `backend/app/main.py`
- Update allowed origins if needed

### API connection issues
- Verify backend URL in `frontend/src/services/api.js`
- Check network tab in browser DevTools
- Ensure both servers are running

## 📚 Key Features

### ✨ Backend Features
- RESTful API design
- Automatic API documentation (Swagger/ReDoc)
- Request validation with Pydantic
- Error handling and logging
- CSV data persistence
- Async/await support

### ✨ Frontend Features
- Single Page Application (SPA)
- Client-side routing
- Real-time data updates
- Responsive design
- Accessible UI components
- Loading states and error handling

### ✨ AI Features
- Personalized user responses
- Review summarization
- Action recommendations
- Multiple prediction approaches

## 🎓 Learning Outcomes

This project demonstrates:
- ✅ Modern Python web development (FastAPI)
- ✅ React frontend development
- ✅ RESTful API design
- ✅ LLM integration (Gemini)
- ✅ UV package management
- ✅ Component-based architecture
- ✅ Neubrutalism design principles
- ✅ Full-stack deployment

## 📄 License

This project is created for the Fynd AI Intern assessment.

## 🤝 Contributing

This is an assessment project, but suggestions are welcome!

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review API documentation at `/docs`
3. Check browser console for frontend errors
4. Review terminal output for backend errors

---

**Built with ❤️ for Fynd AI Intern Assessment**

*Stack: FastAPI + React + Gemini AI + Neubrutalism UI*
