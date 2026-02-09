# 🔧 Render Deployment Troubleshooting Guide

## ❌ Error: "Application exited early"

Based on your logs, the issue is that your Django application is failing to start on Render.

---

## ✅ Solution: Fix Render Configuration

### Step 1: Verify Start Command

In your Render dashboard, ensure the **Start Command** is set to:

```bash
gunicorn config.wsgi:application
```

**NOT** something like `:INTERN-TECHNICAL-ASSIGNMENT.wsgi` or any other variant.

### Step 2: Check Required Environment Variables

Make sure ALL of these environment variables are set in Render:

#### Required Variables:
```bash
SECRET_KEY=<your-generated-secret-key>
DEBUG=False
DATABASE_URL=<render-postgres-internal-url>
ALLOWED_HOSTS=<your-service-name>.onrender.com
```

#### Optional but Recommended:
```bash
FRONTEND_URL=https://your-frontend.vercel.app
LOG_LEVEL=INFO
DJANGO_LOG_LEVEL=INFO
SECURE_SSL_REDIRECT=True
```

**IMPORTANT**: The `DATABASE_URL` should be the **Internal Database URL** from your PostgreSQL database, NOT the external URL.

### Step 3: Verify Build Command

Build command should be:
```bash
sh build.sh
```

OR manually:
```bash
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
```

### Step 4: Check Root Directory

Make sure the **Root Directory** is set to:
```
backend
```

---

## 🔍 Common Issues & Fixes

### Issue 1: Missing SECRET_KEY
**Symptom**: "SECRET_KEY environment variable is not set"

**Fix**: Generate a new secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Add it to Render environment variables.

### Issue 2: Database Connection Failed
**Symptom**: "Connection refused" or "database does not exist"

**Fix**:
1. Ensure PostgreSQL database is created in Render
2. Copy the **Internal Database URL** (starts with `postgresql://` or `postgres://`)
3. Set it as `DATABASE_URL` environment variable
4. Both database and web service should be in the **same region**

### Issue 3: ALLOWED_HOSTS Error
**Symptom**: "DisallowedHost at /"

**Fix**: Set environment variable:
```bash
ALLOWED_HOSTS=your-service-name.onrender.com,localhost,127.0.0.1
```

### Issue 4: Static Files Not Found
**Symptom**: 500 errors, missing CSS/JS

**Fix**: Ensure `build.sh` includes:
```bash
python manage.py collectstatic --no-input
```

---

## 📋 Complete Render Configuration Checklist

### Web Service Settings:
- [x] **Name**: `intern-assignment-backend` (or your choice)
- [x] **Environment**: Python 3
- [x] **Region**: Same as database
- [x] **Branch**: `main`
- [x] **Root Directory**: `backend`
- [x] **Build Command**: `sh build.sh`
- [x] **Start Command**: `gunicorn config.wsgi:application`

### Environment Variables:
- [x] `SECRET_KEY` - Generated, not the dev one
- [x] `DEBUG=False`
- [x] `DATABASE_URL` - Internal PostgreSQL URL
- [x] `ALLOWED_HOSTS` - Your Render domain
- [x] `FRONTEND_URL` - Your Vercel URL (optional)

---

## 🚀 Steps to Redeploy After Fixing

1. **Update Configuration** in Render Dashboard:
   - Go to your web service
   - Click **"Environment"** tab
   - Verify/add all required environment variables
   - Click **"Settings"** tab
   - Verify Start Command: `gunicorn config.wsgi:application`
   - Verify Build Command: `sh build.sh`

2. **Manual Redeploy**:
   - Click **"Manual Deploy"** → **"Clear build cache & deploy"**
   - OR just push to GitHub if auto-deploy is enabled

3. **Monitor Logs**:
   - Watch the deployment logs in real-time
   - Look for successful messages like "Listening at: http://0.0.0.0:10000"

---

## ✅ Expected Success Logs

You should see:
```
==> Building...
==> Installing dependencies...
==> Running migrations...
==> Collecting static files...
==> Build successful 🎉
==> Deploying...
==> Starting gunicorn...
==> Listening at: http://0.0.0.0:10000
```

Then your health check should work:
```bash
curl https://your-service.onrender.com/api/health/
# Expected: {"status":"healthy","database":"connected","debug":false}
```

---

## 📞 Still Having Issues?

If the deployment still fails:

1. **Check Render Logs** for the exact error message
2. **Verify Database** is running and accessible
3. **Test Locally** with production settings:
   ```bash
   cd backend
   set DEBUG=False
   set SECRET_KEY=test-key-at-least-fifty-chars-long-for-testing
   set DATABASE_URL=sqlite:///db.sqlite3
   set ALLOWED_HOSTS=localhost
   python manage.py check --deploy
   gunicorn config.wsgi:application
   ```

4. Share the **complete error logs** if you need more help

---

## 🔗 Useful Resources

- [Render Python Docs](https://render.com/docs/deploy-django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- Your project's [DEPLOYMENT.md](file:///d:/INTERN-TECHNICAL-ASSIGNMENT-b/DEPLOYMENT.md)
