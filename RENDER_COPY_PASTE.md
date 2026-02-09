# 🎯 RENDER DEPLOYMENT - COPY & PASTE CONFIGURATION

## ✅ STEP 1: SETTINGS TAB

### Build Command (copy this):
```
pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input
```

### Start Command (copy this):
```
gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
```

### Root Directory (verify):
```
backend
```

---

## ✅ STEP 2: ENVIRONMENT TAB

Copy these environment variables:

### SECRET_KEY
```
[GENERATED BELOW - SEE OUTPUT]
```

### DEBUG
```
False
```

### DATABASE_URL
```
[YOUR POSTGRES INTERNAL URL - Get from your PostgreSQL database in Render]
```

### ALLOWED_HOSTS
```
[YOUR-SERVICE-NAME].onrender.com
```
Replace `[YOUR-SERVICE-NAME]` with your actual Render service name (e.g., `intern-assignment-backend`)

### PYTHON_VERSION
```
3.11.7
```

### FRONTEND_URL (Optional)
```
https://[YOUR-VERCEL-URL].vercel.app
```

---

## 🚀 STEP 3: DEPLOY

1. Click "Save Changes" 
2. Click "Manual Deploy" → "Clear build cache & deploy"
3. Wait for success!

---

## 📋 QUICK CHECKLIST

In Render Dashboard:

- [ ] Go to your web service
- [ ] Settings tab → Update Build Command
- [ ] Settings tab → Update Start Command  
- [ ] Settings tab → Verify Root Directory = `backend`
- [ ] Environment tab → Add all 5 environment variables above
- [ ] Click "Manual Deploy" → "Clear build cache & deploy"

---

## ✅ SUCCESS CHECK

After deployment, visit:
```
https://[your-service].onrender.com/api/health/
```

Should return:
```json
{"status":"healthy","database":"connected","debug":false}
```

---

**Note**: Unfortunately, I cannot access your Render dashboard directly - you'll need to copy these values into Render's web interface. It takes about 2 minutes! 🚀
