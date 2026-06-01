# 🚀 Makpost Deployment Guide

This guide covers deploying **makpost** to production using **Railway** (backend) and **Vercel** (frontend).

---

## 📋 Prerequisites

- GitHub account with repository access
- Railway account (https://railway.app)
- Vercel account (https://vercel.com)
- PostgreSQL database (Railway provides this)

---

## 🔧 Backend Deployment (Django + Railway)

### Step 1: Prepare Your Repository

1. **Add `.env` to `.gitignore`**
   - Ensure `.env` is in `.gitignore` (already done)
   - Never commit sensitive credentials

2. **Check all files are committed:**
   ```bash
   git add .
   git commit -m "Prepare for production deployment"
   git push origin main
   ```

### Step 2: Deploy to Railway

1. **Go to https://railway.app and sign in with GitHub**

2. **Create a new project:**
   - Click "Create Project"
   - Select "Deploy from GitHub repo"
   - Choose `Lonelyhackertechs/makpost`
   - Click "Deploy"

3. **Add PostgreSQL database:**
   - In Railway dashboard, click "Add Plugin"
   - Select "PostgreSQL"
   - Connect to your app

4. **Configure Environment Variables:**
   - Go to your app settings
   - Add these variables:

   ```
   DEBUG=False
   SECRET_KEY=<generate-a-new-secure-key>
   ALLOWED_HOSTS=your-domain.railway.app,yourdomain.com,www.yourdomain.com
   DATABASE_URL=<Railway auto-generates this>
   CORS_ALLOWED_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   FRONTEND_URL=https://yourdomain.com
   ```

5. **Generate a secure SECRET_KEY:**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

6. **Railway will automatically:**
   - Install dependencies from `requirements.txt`
   - Run migrations (via `Procfile`)
   - Start the Gunicorn server
   - Provide a public URL like `https://makpost-production.railway.app`

7. **Your backend will be at:**
   ```
   https://your-backend-url.railway.app
   ```

---

## 🎨 Frontend Deployment (React + Vercel)

### Step 1: Prepare Your Repository

The repository already has `vercel.json` configured.

### Step 2: Deploy to Vercel

1. **Go to https://vercel.com and sign in with GitHub**

2. **Import your repository:**
   - Click "Add New"
   - Select "Project"
   - Find `Lonelyhackertechs/makpost`
   - Click "Import"

3. **Configure Build Settings:**
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
   - **Install Command:** `npm install`

4. **Add Environment Variables:**
   - In Vercel settings, go to "Environment Variables"
   - Add:
     ```
     VITE_API_URL=https://your-backend-url.railway.app
     VITE_API_BASE=/api
     ```
     (Use the Railway backend URL you got earlier)

5. **Deploy:**
   - Click "Deploy"
   - Vercel will automatically build and deploy
   - You'll get a URL like `https://makpost.vercel.app`

6. **Your frontend will be at:**
   ```
   https://makpost.vercel.app
   (or your custom domain)
   ```

---

## 🌐 Custom Domain Setup (Optional)

### For Backend (Railway):
1. In Railway dashboard, go to "Settings"
2. Add "Custom Domain"
3. Point DNS to Railway's servers

### For Frontend (Vercel):
1. In Vercel project settings, go to "Domains"
2. Add your custom domain
3. Follow Vercel's DNS instructions

---

## 🔗 Frontend-Backend Integration

After deployment, update your React app's API endpoint:

**In your React code (API service):**
```javascript
const API_URL = process.env.VITE_API_URL || 'https://your-backend-url.railway.app';
const API_BASE = process.env.VITE_API_BASE || '/api';

export const API = axios.create({
  baseURL: `${API_URL}${API_BASE}`,
});
```

---

## ✅ Testing After Deployment

1. **Test backend API:**
   ```bash
   curl https://your-backend-url.railway.app/api/posts/
   ```

2. **Test frontend:**
   - Open https://your-frontend-url.vercel.app
   - Try registering a new user
   - Create a post
   - Check if API calls succeed

3. **Check browser console for CORS errors**
   - If you see CORS errors, update `CORS_ALLOWED_ORIGINS` in Railway

---

## 🐛 Troubleshooting

### Backend won't start
- Check Railway logs: `railway logs`
- Ensure all env variables are set
- Verify database connection

### CORS errors on frontend
- Update `CORS_ALLOWED_ORIGINS` in Django settings
- Restart Railway deployment

### Static files not loading
- Run: `cd webmak && python manage.py collectstatic --noinput`
- Rebuild on Railway

### Database migrations not running
- Railway auto-runs migrations via `Procfile`
- Check release logs in Railway

---

## 📝 Production Checklist

- ✅ `DEBUG = False`
- ✅ `SECRET_KEY` is unique and secure
- ✅ `ALLOWED_HOSTS` includes your domain
- ✅ Database is PostgreSQL
- ✅ CORS is properly configured
- ✅ Environment variables are set
- ✅ `.env` is in `.gitignore`
- ✅ Frontend `VITE_API_URL` points to production backend
- ✅ HTTPS is enabled (automatic on Railway & Vercel)
- ✅ Backups are configured

---

## 📞 Support

For issues:
1. Check Railway logs: `railway logs`
2. Check Vercel build logs
3. Open a GitHub issue: [Issues](https://github.com/Lonelyhackertechs/makpost/issues)

**Recommended platforms:**
- **Backend:** Railway (easy PostgreSQL setup, Procfile support)
- **Frontend:** Vercel (React-optimized, automatic deployments from GitHub)

---

**Happy deploying! 🚀**