# 🚀 Deployment Guide - FastAPI + React Stack

Complete deployment guide for the Fynd AI Assessment project.

## 📋 Table of Contents

1. [Backend Deployment (Render)](#backend-deployment-render)
2. [Backend Deployment (Railway)](#backend-deployment-railway)
3. [Frontend Deployment (Vercel)](#frontend-deployment-vercel)
4. [Frontend Deployment (Netlify)](#frontend-deployment-netlify)
5. [Full-Stack Deployment (Docker)](#full-stack-deployment-docker)
6. [Environment Configuration](#environment-configuration)
7. [Post-Deployment Testing](#post-deployment-testing)

---

## Backend Deployment (Render)

### Step 1: Prepare Backend

Create `backend/render.yaml`:

```yaml
services:
  - type: web
    name: fynd-ai-backend
    env: python
    region: oregon
    plan: free
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: GEMINI_API_KEY
        sync: false
      - key: PYTHON_VERSION
        value: 3.11.0
```

### Step 2: Deploy to Render

1. **Sign up** at https://render.com
2. **New → Web Service**
3. **Connect GitHub** repository
4. **Configure**:
   - **Name**: fynd-ai-backend
   - **Root Directory**: backend
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variable**:
   - Key: `GEMINI_API_KEY`
   - Value: `AIzaSyA6ZQ-hgxvl0_eQvLQmTa45NUlR6MzUulg`
6. **Create Web Service**

### Step 3: Get Backend URL

After deployment completes:
- URL format: `https://fynd-ai-backend.onrender.com`
- Test: `https://fynd-ai-backend.onrender.com/health`
- API Docs: `https://fynd-ai-backend.onrender.com/docs`

---

## Backend Deployment (Railway)

### Step 1: Prepare Backend

Create `backend/railway.toml`:

```toml
[build]
builder = "NIXPACKS"
buildCommand = "pip install -r requirements.txt"

[deploy]
startCommand = "uvicorn app.main:app --host 0.0.0.0 --port $PORT"
restartPolicyType = "ON_FAILURE"
restartPolicyMaxRetries = 10
```

### Step 2: Deploy to Railway

1. **Sign up** at https://railway.app
2. **New Project → Deploy from GitHub**
3. **Select** repository
4. **Add variables**:
   ```
   GEMINI_API_KEY=AIzaSyA6ZQ-hgxvl0_eQvLQmTa45NUlR6MzUulg
   PORT=8000
   ```
5. **Deploy**

### Step 3: Configure

- **Root Directory**: Set to `backend` in settings
- **Custom Domain** (optional): Add your domain
- **Health Checks**: Enable at `/health`

---

## Frontend Deployment (Vercel)

### Step 1: Prepare Frontend

Create `frontend/vercel.json`:

```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "build",
  "devCommand": "npm start",
  "installCommand": "npm install",
  "framework": "create-react-app",
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

### Step 2: Update API URL

In `frontend/src/services/api.js`, update:

```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';
```

### Step 3: Deploy to Vercel

1. **Sign up** at https://vercel.com
2. **New Project**
3. **Import** GitHub repository
4. **Configure**:
   - **Framework Preset**: Create React App
   - **Root Directory**: frontend
   - **Build Command**: `npm run build`
   - **Output Directory**: build
5. **Environment Variables**:
   ```
   REACT_APP_API_URL=https://fynd-ai-backend.onrender.com/api
   ```
6. **Deploy**

### Step 4: Get Frontend URL

After deployment:
- URL: `https://your-project.vercel.app`
- Automatic HTTPS
- Auto-deploys on git push

---

## Frontend Deployment (Netlify)

### Step 1: Prepare Frontend

Create `frontend/netlify.toml`:

```toml
[build]
  base = "frontend/"
  command = "npm run build"
  publish = "build/"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[build.environment]
  NODE_VERSION = "18"
```

### Step 2: Deploy to Netlify

1. **Sign up** at https://netlify.com
2. **New Site from Git**
3. **Connect** GitHub repository
4. **Build Settings**:
   - **Base directory**: frontend
   - **Build command**: `npm run build`
   - **Publish directory**: frontend/build
5. **Environment Variables**:
   - Go to **Site settings → Environment variables**
   - Add: `REACT_APP_API_URL=https://fynd-ai-backend.onrender.com/api`
6. **Deploy Site**

### Step 3: Configure

- **Domain**: Set custom domain (optional)
- **HTTPS**: Automatically enabled
- **Continuous Deployment**: Enabled by default

---

## Full-Stack Deployment (Docker)

### Step 1: Create Dockerfiles

**backend/Dockerfile**:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**frontend/Dockerfile**:

```dockerfile
FROM node:18-alpine as build

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

**frontend/nginx.conf**:

```nginx
server {
    listen 80;
    server_name localhost;
    
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;
    }
    
    location /api {
        proxy_pass http://backend:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### Step 2: Create Docker Compose

**docker-compose.yml**:

```yaml
version: '3.8'

services:
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    container_name: fynd-backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
    volumes:
      - ./backend/data:/app/data
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile
    container_name: fynd-frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    restart: unless-stopped
```

### Step 3: Deploy

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## Environment Configuration

### Backend .env

```env
# Required
GEMINI_API_KEY=AIzaSyA6ZQ-hgxvl0_eQvLQmTa45NUlR6MzUulg

# Optional
PORT=8000
HOST=0.0.0.0
CORS_ORIGINS=*
LOG_LEVEL=info
```

### Frontend .env

```env
# Production
REACT_APP_API_URL=https://your-backend-url.com/api

# Development
REACT_APP_API_URL=http://localhost:8000/api
```

### Production Security

**Update CORS in backend/app/main.py**:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-frontend.vercel.app",
        "https://your-custom-domain.com"
    ],  # Replace * with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Post-Deployment Testing

### 1. Health Check

```bash
# Backend
curl https://your-backend-url.com/health

# Expected: {"status":"healthy"}
```

### 2. API Testing

```bash
# Submit review
curl -X POST https://your-backend-url.com/api/reviews/submit \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "test",
    "review_text": "Great service!",
    "stars": 5,
    "user_id": "test_user"
  }'
```

### 3. Frontend Testing

1. Open https://your-frontend-url.com
2. Submit a review
3. Check Admin dashboard
4. Verify charts load
5. Test AI insights generation

### 4. Performance Testing

```bash
# Load test (using Apache Bench)
ab -n 100 -c 10 https://your-backend-url.com/api/reviews/all
```

### 5. Monitoring

**Render**:
- View logs in dashboard
- Check metrics
- Set up alerts

**Vercel**:
- Analytics dashboard
- Real-time logs
- Performance insights

**Railway**:
- Metrics tab
- Logs viewer
- Resource usage

---

## Deployment Checklist

### Pre-Deployment

- [ ] Test locally with production settings
- [ ] Update CORS origins
- [ ] Set environment variables
- [ ] Test API endpoints
- [ ] Build frontend successfully
- [ ] Run tests

### Backend Deployment

- [ ] Deploy to Render/Railway
- [ ] Add GEMINI_API_KEY
- [ ] Verify health check
- [ ] Test API docs (/docs)
- [ ] Check logs for errors

### Frontend Deployment

- [ ] Deploy to Vercel/Netlify
- [ ] Set REACT_APP_API_URL
- [ ] Verify build completes
- [ ] Test user page
- [ ] Test admin dashboard
- [ ] Check console for errors

### Post-Deployment

- [ ] Test full user flow
- [ ] Verify AI responses work
- [ ] Check analytics display
- [ ] Test on mobile
- [ ] Monitor for errors
- [ ] Update README with URLs

---

## Troubleshooting

### Backend Issues

**Build fails**:
```bash
# Check Python version
python --version  # Should be 3.10+

# Install dependencies locally
pip install -r backend/requirements.txt
```

**API returns 500**:
- Check GEMINI_API_KEY is set
- Review logs for stack trace
- Verify data directory exists

### Frontend Issues

**Build fails**:
```bash
# Clear cache
npm cache clean --force

# Reinstall
rm -rf node_modules package-lock.json
npm install
```

**API connection fails**:
- Check REACT_APP_API_URL is correct
- Verify CORS settings
- Check Network tab in DevTools

### CORS Errors

Update `backend/app/main.py`:
```python
allow_origins=["https://your-frontend.vercel.app"]
```

Redeploy backend.

---

## Monitoring & Maintenance

### Log Monitoring

**Render**:
```bash
# View logs
render logs --tail

# Watch logs
render logs --follow
```

**Railway**:
- Logs tab in dashboard
- Real-time streaming
- Filter by service

### Performance

- Use CDN for static assets
- Enable caching headers
- Compress responses (gzip)
- Optimize images
- Monitor API response times

### Security

- Keep dependencies updated
- Use HTTPS only
- Rotate API keys periodically
- Monitor for vulnerabilities
- Set rate limiting

---

## Cost Optimization

### Free Tier Limits

**Render**:
- 750 hours/month
- Sleeps after 15 min inactivity
- 512 MB RAM

**Railway**:
- $5 free credit/month
- Usage-based billing
- Automatic scaling

**Vercel**:
- 100 GB bandwidth
- Unlimited deployments
- Serverless functions

**Netlify**:
- 100 GB bandwidth
- 300 build minutes/month
- Instant cache invalidation

### Tips

- Use caching effectively
- Optimize bundle size
- Minimize API calls
- Use lazy loading
- Compress responses

---

## Next Steps

1. ✅ Deploy backend
2. ✅ Deploy frontend
3. ✅ Update CORS
4. ✅ Test thoroughly
5. ✅ Monitor performance
6. ✅ Set up custom domain (optional)
7. ✅ Enable analytics
8. ✅ Add monitoring alerts

---

**Deployment Complete! 🎉**

Your Fynd AI Assessment project is now live!
