# 🚨 RENDER DEPLOYMENT - QUICK FIX GUIDE

## ❌ Current Error
**"Application exited early while running your code"**

Render is trying to use **Poetry** instead of **pip**. This is the wrong build system for our project.

---

## ✅ EXACT CONFIGURATION NEEDED

### **In Render Dashboard → Your Web Service → Settings**

Copy these settings **EXACTLY**:

| Setting | Value |
|---------|-------|
| **Name** | `intern-assignment-backend` |
| **Region** | Choose one (e.g., Oregon, Ohio) |
| **Branch** | `main` |
| **Root Directory** | `backend` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input` |
| **Start Command** | `gunicorn config.wsgi:application --bind 0.0.0.0:$PORT` |

---

## 🔑 REQUIRED ENVIRONMENT VARIABLES

### In Render Dashboard → Your Web Service → Environment

Add these one by one:

```bash
SECRET_KEY=django-insecure-GENERATE-A-NEW-ONE-AT-LEAST-50-CHARS-LONG-abcd1234
DEBUG=False
DATABASE_URL=<paste-your-postgres-internal-url-here>
ALLOWED_HOSTS=intern-assignment-backend.onrender.com
FRONTEND_URL=https://your-frontend.vercel.app
PYTHON_VERSION=3.11.7
```

### 🔐 How to Generate SECRET_KEY

Run this locally:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Copy the output and use it as `SECRET_KEY`.

### 📊 How to Get DATABASE_URL

1. Go to your PostgreSQL database in Render
2. Copy the **Internal Database URL** (NOT External)
3. It should look like: `postgresql://user:password@dpg-xxx-a/dbname`

---

## 🎯 WHY build.sh ISN'T WORKING

Render auto-detects build systems in this order:
1. Poetry (if `pyproject.toml` exists)
2. Pipenv (if `Pipfile` exists)  
3. pip (if `requirements.txt` exists)

Since we don't want auto-detection, we're **explicitly specifying the build command** instead of using `sh build.sh`.

---

## 📝 STEP-BY-STEP FIX

### Step 1: Update Build Command
1. Go to Render Dashboard
2. Click on your web service
3. Go to **Settings** tab
4. Scroll to **Build Command**
5. **Delete** the current value
6. **Paste** this:
   ```
   pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
   ```
7. Click **Save Changes**

### Step 2: Update Start Command
1. Still in **Settings** tab
2. Scroll to **Start Command**
3. **Delete** the current value
4. **Paste** this:
   ```
   gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
   ```
5. Click **Save Changes**

### Step 3: Verify Root Directory
1. Still in **Settings** tab
2. Scroll to **Root Directory**
3. Ensure it says: `backend`
4. If not, change it and click **Save Changes**

### Step 4: Add Environment Variables
1. Go to **Environment** tab
2. Click **Add Environment Variable**
3. Add each variable from the list above
4. Click **Save Changes** after adding all

### Step 5: Deploy
1. Click **Manual Deploy** button (top right)
2. Select **Clear build cache & deploy**
3. Wait and watch the logs

---

## ✅ EXPECTED SUCCESS LOGS

You should see:
```
==> Cloning from https://github.com/...
==> Installing Python version 3.11.7...
==> Running 'pip install -r requirements.txt && ...'
==> Successfully installed Django-5.0.1 djangorestframework-3.16.1 ...
==> Running migrations...
==> Collecting static files...
==> Build successful 🎉
==> Starting gunicorn...
==> [INFO] Listening at: http://0.0.0.0:10000
```

---

## 🧪 TEST YOUR DEPLOYMENT

Once deployed, test these URLs:

### Health Check
```bash
curl https://intern-assignment-backend.onrender.com/api/health/
```
**Expected response:**
```json
{"status":"healthy","database":"connected","debug":false}
```

### Facts API
```bash
curl https://intern-assignment-backend.onrender.com/api/facts/
```
**Expected response:**
```json
{"success":true,"count":10,"message":"Facts retrieved successfully","data":[...]}
```

---

## 🐛 STILL FAILING?

### Check These:

1. **Database is Running**
   - Go to your PostgreSQL database in Render
   - Status should be "Available"

2. **Database and Web Service in Same Region**
   - Both should be in same region (e.g., both in Oregon)

3. **Environment Variables are Set**
   - All 5 required variables must be present
   - No typos in variable names
   - `DATABASE_URL` is the **Internal** URL

4. **Share Full Logs**
   - Copy the complete deployment logs
   - Look for the actual error message (usually after "Running")

---

## 📸 SCREENSHOT GUIDE

Your deployment settings should look like this:

**Settings Tab:**
```
Build Command: pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
Start Command: gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
Root Directory: backend
```

**Environment Tab:**
```
SECRET_KEY: django-insecure-xxx...
DEBUG: False
DATABASE_URL: postgresql://xxx...
ALLOWED_HOSTS: your-service.onrender.com
FRONTEND_URL: https://your-frontend.vercel.app
PYTHON_VERSION: 3.11.7
```

---

## 💡 IMPORTANT NOTES

- ⚠️ **First deployment** takes 3-5 minutes
- ⚠️ **Free tier** spins down after 15 min inactivity (first request takes 50+ seconds)
- ✅ Once these settings are correct, **future deployments will work automatically**
- ✅ You can return to using `sh build.sh` after first successful deployment if you prefer

---

**Need help? Share:**
1. Screenshot of your Settings tab
2. Screenshot of your Environment tab
3. Full deployment logs (the text, not just screenshot)
