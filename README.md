# 🎯 Full-Stack Mini Project - Django + React

## 📌 Project Overview
**Complete full-stack web application** showcasing:
- **Backend**: Django + Django REST Framework
- **Frontend**: React with Hooks
- **Database**: SQLite
- **API**: RESTful architecture

## 🌐 Live Deployment
- **Frontend**: https://intern-technical-assignment.vercel.app/
- **Backend API**: https://intern-technical-assignment.onrender.com/api/facts/
- **Status**: ✅ Fully Integrated & Deployed

---

## 📂 Project Structure

```
INTERN TECHNICAL ASSIGNMENT b/
│
├── backend/                    # Django Backend ✅
│   ├── config/                # Project settings
│   │   ├── settings.py       # Main configuration
│   │   └── urls.py           # Project routing
│   │
│   ├── api/                   # REST API app
│   │   ├── views.py          # API endpoints ✅
│   │   └── urls.py           # App routing ✅
│   │
│   ├── manage.py
│   ├── db.sqlite3
│   └── requirements.txt
│
├── frontend/                  # React Frontend ✅
│   ├── src/
│   │   ├── App.js            # Main component
│   │   └── App.css           # Styling
│   │
│   ├── package.json
│   └── README.md
│
└── venv/                      # Python virtual environment
```

---

## 🚀 Quick Start

### 1. Start Django Backend
```bash
# Activate virtual environment
.\venv\Scripts\activate

# Navigate and run server
cd backend
python manage.py runserver
```
**Runs at**: http://127.0.0.1:8000/

### 2. Start React Frontend
```bash
# In a new terminal
cd frontend
npm start
```
**Runs at**: http://localhost:3001/

---

## 🎯 Completed Steps

### ✅ STEP 1: Backend Setup
- Virtual environment created
- Django & DRF installed
- Database migrated
- Admin user created

### ✅ STEP 2: API Development  
- REST endpoint: `GET /api/facts/`
- Returns 10 hardcoded facts
- CORS configured
- JSON response format

### ✅ STEP 3: Frontend Development
- React app created
- API integration complete
- useState & useEffect hooks
- Responsive UI design
- Error handling & loading states

---

## 🌐 API Endpoint

```
GET http://127.0.0.1:8000/api/facts/
```

**Response:**
```json
{
  "success": true,
  "count": 10,
  "message": "Facts retrieved successfully",
  "data": [
    {
      "id": 1,
      "fact": "Python was named after Monty Python...",
      "category": "Programming"
    }
  ]
}
```

---

## 🔑 Admin Access

- **URL**: http://127.0.0.1:8000/admin/
- **Username**: admin
- **Password**: admin123

---

## 📦 Dependencies

### Backend
```
Django==5.0.1
djangorestframework==3.16.1
django-cors-headers==4.9.0
```

### Frontend
```
React 19.2.4
React DOM 19.2.4
```

---

## 🎨 Features

### Backend
- ✅ RESTful API
- ✅ CORS enabled
- ✅ Structured JSON responses
- ✅ Admin panel

### Frontend
- ✅ React Hooks (useState, useEffect)
- ✅ Fetch API integration
- ✅ Loading spinner
- ✅ Error handling
- ✅ Responsive cards layout
- ✅ Purple gradient design
- ✅ Mobile-friendly

---

## 🛠️ Key Files

| File | Purpose |
|------|---------|
| `backend/api/views.py` | API endpoint logic |
| `backend/api/urls.py` | API routing |
| `backend/config/settings.py` | Django configuration |
| `backend/config/urls.py` | Project routing |
| `frontend/src/App.js` | React main component |
| `frontend/src/App.css` | Component styling |

---

## 📚 Learning Outcomes

**Backend Skills:**
- Django REST Framework
- API endpoint creation
- CORS configuration
- URL routing

**Frontend Skills:**
- React functional components
- React Hooks (useState, useEffect)
- Fetch API
- Async/await
- Error handling
- Responsive CSS

**Full-Stack:**
- Client-server communication
- RESTful API design
- JSON data exchange
- Cross-origin requests

---

## 🔧 Configuration

### Environment Variables

#### Backend Environment Variables
Create a `.env` file in the `backend/` directory (see `.env.example` for template):

```bash
# Production settings
SECRET_KEY=your-secret-key-here-must-be-at-least-50-characters-long
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
DATABASE_URL=postgres://user:password@host:port/database

# CORS configuration
FRONTEND_URL=https://your-frontend.vercel.app

# Logging
LOG_LEVEL=INFO
DJANGO_LOG_LEVEL=INFO

# SSL (set to False for local development)
SECURE_SSL_REDIRECT=False
```

**Generate a new SECRET_KEY**:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### Frontend Environment Variables
**Frontend** uses environment-specific API URLs:

- **Production** (`.env.production`):
  ```
  REACT_APP_API_URL=https://your-backend.onrender.com/api/facts/
  ```

- **Development** (`.env.development`):
  ```
  REACT_APP_API_URL=http://127.0.0.1:8000/api/facts/
  ```

### API URL Configuration
**File**: `frontend/src/App.js`
```javascript
const API_URL = process.env.REACT_APP_API_URL || 'https://intern-technical-assignment.onrender.com/api/facts/';
```

---

## 🚀 Production Deployment

### Quick Deploy

**Backend (Render)**:
1. Create PostgreSQL database
2. Deploy web service with `backend/` as root directory
3. Set environment variables (SECRET_KEY, DATABASE_URL, etc.)
4. Use `gunicorn config.wsgi:application` as start command

**Frontend (Vercel)**:
1. Import GitHub repository
2. Set root directory to `frontend/`
3. Add `REACT_APP_API_URL` environment variable
4. Deploy

### Detailed Instructions
📖 **See [DEPLOYMENT.md](./DEPLOYMENT.md)** for complete step-by-step deployment guide including:
- PostgreSQL setup on Render
- Environment variable configuration
- Custom domain setup
- Troubleshooting common issues
- Security best practices

### Health Check
After deployment, verify backend health:
```bash
curl https://your-backend.onrender.com/api/health/
# Expected: {"status": "healthy", "database": "connected", "debug": false}

---

## 🔍 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
python manage.py runserver 8001
```

### "Failed to fetch" error
```bash
# Ensure Django is running
cd backend
python manage.py runserver
```

### CORS errors
Check `backend/config/settings.py`:
- CORS headers in INSTALLED_APPS
- CORS middleware enabled
- Correct origins in CORS_ALLOWED_ORIGINS

### Port 3000 already in use
React will prompt to use another port - type 'Y'

---

## ✅ Project Status

**Status**: ✅ **PRODUCTION READY** - Ready for deployment to Render + Vercel

- [x] Virtual environment setup
- [x] Django project created
- [x] API app created  
- [x] Database migrations
- [x] Admin user created
- [x] API endpoint implemented
- [x] CORS configured
- [x] React app created
- [x] API integration
- [x] UI components
- [x] Error handling
- [x] Responsive design
- [x] **Production settings configured**
- [x] **PostgreSQL support added**
- [x] **Security hardening (DEBUG=False, SECRET_KEY from env)**
- [x] **Static files configuration (WhiteNoise)**
- [x] **Health check endpoint**
- [x] **Deployment files (build.sh, runtime.txt)**
- [x] **Vercel configuration**
- [x] **Comprehensive deployment guide**

---

## 📞 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [React Documentation](https://react.dev/)
- [Fetch API Guide](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

---

**Last Updated**: February 9, 2026  
**Project Type**: Full-Stack Internship Assessment  
**Status**: ✅ **Production Ready - Deploy to Render + Vercel**  
**Deployment Guide**: [DEPLOYMENT.md](./DEPLOYMENT.md)
