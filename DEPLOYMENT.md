# 🚀 Deployment Guide - Django + React

Complete step-by-step guide to deploy the full-stack application to production.

## 📋 Prerequisites

- GitHub repository with your code
- [Render](https://render.com) account (free tier available)
- [Vercel](https://vercel.com) account (free tier available)

---

## 🔧 Part 1: Backend Deployment (Render)

### Step 1: Create PostgreSQL Database

1. Log in to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"PostgreSQL"**
3. Configure database:
   - **Name**: `intern-assignment-db` (or your preferred name)
   - **Database**: `intern_assignment`
   - **User**: (auto-generated)
   - **Region**: Choose closest to your users
   - **Plan**: **Free**
4. Click **"Create Database"**
5. **IMPORTANT**: Copy the **Internal Database URL** from the database info page
   - Format: `postgres://user:password@host/database`
   - You'll need this for the backend environment variables

### Step 2: Deploy Backend (Web Service)

1. In Render Dashboard, click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `intern-assignment-backend`
   - **Region**: Same as database
   - **Branch**: `main` (or your deployment branch)
   - **Root Directory**: `backend`
   - **Environment**: **Python 3**
   - **Build Command**: `sh build.sh`
   - **Start Command**: `gunicorn config.wsgi:application`
   - **Plan**: **Free**

4. **Environment Variables** - Add these in Render:
   ```
   SECRET_KEY=<generate-new-secret-key-here>
   DEBUG=False
   DATABASE_URL=<paste-internal-database-url-from-step-1>
   ALLOWED_HOSTS=<your-render-service-url>.onrender.com
   FRONTEND_URL=<will-add-after-vercel-deployment>
   ```

   **Generate SECRET_KEY**:
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. Click **"Create Web Service"**
6. Wait for deployment to complete (first deploy takes 3-5 minutes)
7. **Test the API**:
   - Visit: `https://your-service.onrender.com/api/health/`
   - Should return: `{"status": "healthy", "database": "connected", "debug": false}`
   - Visit: `https://your-service.onrender.com/api/facts/`
   - Should return JSON with facts data

### Step 3: Update Backend Environment Variables

1. After Vercel deployment (next section), return to Render
2. Go to your web service → **Environment** tab
3. Update `FRONTEND_URL` with your Vercel URL
4. Click **"Save Changes"** (this will redeploy)

---

## 🎨 Part 2: Frontend Deployment (Vercel)

### Step 1: Deploy to Vercel

1. Log in to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`
   - **Install Command**: `npm install`

5. **Environment Variables** - Add in Vercel:
   ```
   REACT_APP_API_URL=https://your-render-service.onrender.com/api/facts/
   ```
   Replace `your-render-service` with your actual Render service URL

6. Click **"Deploy"**
7. Wait for deployment (takes 1-2 minutes)
8. Test your frontend at: `https://your-project.vercel.app`

### Step 2: Configure Custom Domain (Optional)

1. In Vercel, go to **Settings** → **Domains**
2. Add your custom domain
3. Update DNS records as instructed
4. Don't forget to update `FRONTEND_URL` in Render backend!

---

## ✅ Part 3: Verification

### Backend Health Check
```bash
curl https://your-service.onrender.com/api/health/
# Expected: {"status": "healthy", "database": "connected", "debug": false}
```

### API Endpoint Test
```bash
curl https://your-service.onrender.com/api/facts/
# Expected: JSON response with 10 facts
```

### Frontend Test
1. Visit your Vercel URL
2. Should see facts loading from backend
3. Open browser console - should have NO CORS errors
4. Should see: `✅ Facts fetched successfully`

### Security Verification
- ✅ No Django debug page on errors
- ✅ HTTPS enforced on both platforms
- ✅ No exposed SECRET_KEY in code
- ✅ Database credentials from environment only

---

## 🔄 Continuous Deployment

### Automatic Deployments
Both Render and Vercel support automatic deployments:
- **Push to GitHub** → Automatically deploys to production
- Configure in platform settings if needed

### Manual Redeployment
**Render**: Dashboard → Your Service → "Manual Deploy" → Select branch
**Vercel**: Dashboard → Your Project → Deployments → "Redeploy"

---

## 🐛 Troubleshooting

### Backend Issues

**"Application failed to respond"**
- Check Render logs: Dashboard → Service → Logs
- Verify all environment variables are set correctly
- Ensure `build.sh` has execute permissions

**Database connection failed**
- Verify `DATABASE_URL` is the **Internal Database URL**
- Check database is running in Render dashboard
- Ensure both services are in the same region

**Static files not loading**
- Run `python manage.py collectstatic` is in build.sh ✓
- WhiteNoise is in `requirements.txt` and `MIDDLEWARE` ✓

### Frontend Issues

**"Failed to fetch" error**
- Check `REACT_APP_API_URL` environment variable in Vercel
- Verify backend is accessible at the URL
- Check CORS configuration in Django `settings.py`

**Blank page after deployment**
- Check Vercel build logs for errors
- Verify `vercel.json` rewrites are configured
- Ensure `build` directory is set as output

**API not found (404)**
- Verify API URL in `.env.production`
- Check that environment variable is loaded (restart Vercel deployment)
- Test API endpoint directly in browser

### CORS Errors

**"Access blocked by CORS policy"**
1. Verify `FRONTEND_URL` is set in Render backend
2. Check `CORS_ALLOWED_ORIGINS` includes your Vercel URL
3. Redeploy backend after changing environment variables

---

## 📊 Monitoring

### Render Monitoring
- **Logs**: Real-time application logs
- **Metrics**: CPU, Memory usage
- **Events**: Deployment history

### Vercel Analytics
- **Overview**: Deployment status
- **Logs**: Build and function logs
- **Insights**: Performance metrics (paid feature)

---

## 💰 Cost Considerations

### Free Tier Limits

**Render Free Tier**:
- Sleeps after 15 minutes of inactivity
- 750 hours/month
- PostgreSQL: 90-day data retention

**Vercel Free Tier**:
- 100GB bandwidth/month
- Unlimited deployments

### Keep Backend Awake
To prevent sleeping (optional):
- Use a uptime monitoring service (UptimeRobot, etc.)
- Ping health endpoint every 10 minutes
- Consider upgrading for production applications

---

## 🔐 Security Best Practices

1. ✅ Never commit `.env` files with real credentials
2. ✅ Use separate SECRET_KEY for production
3. ✅ Keep DEBUG=False in production
4. ✅ Use HTTPS only (enforced by both platforms)
5. ✅ Regularly update dependencies
6. ✅ Monitor logs for suspicious activity
7. ✅ Use strong database passwords
8. ✅ Limit ALLOWED_HOSTS to your actual domains

---

## 📚 Additional Resources

- [Render Django Guide](https://render.com/docs/deploy-django)
- [Vercel Deployments](https://vercel.com/docs/deployments)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/stable/howto/deployment/checklist/)
- [Create React App Deployment](https://create-react-app.dev/docs/deployment/)

---

**Ready to Deploy? Start with Part 1! 🚀**
