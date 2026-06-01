# 🆓 FREE HOSTING OPTIONS FOR MAKPOST (Class Project)

**Date:** June 1, 2026  
**Status:** Configure for Free Hosting Platforms  
**Best Options for Students:** Render, Vercel (Free Tier), Netlify

---

## ✅ COMPLETELY FREE HOSTING PLATFORMS

### 🏆 BEST OPTION: Render + Vercel (Recommended)

#### **Backend: Render.com** ✅
- **Cost:** FREE tier available
- **Database:** PostgreSQL included (free)
- **Features:**
  - No credit card needed
  - Auto-deploys from GitHub
  - Free SSL/HTTPS
  - Automatic migrations
  - 750 hours/month free (always on within quota)
- **URL Example:** `https://makpost-backend.onrender.com`

#### **Frontend: Vercel** ✅
- **Cost:** FREE tier
- **Features:**
  - Optimized for React/Vite
  - No credit card needed
  - Unlimited deployments
  - Free SSL/HTTPS
  - Auto-deploys from GitHub
- **URL Example:** `https://makpost.vercel.app`

---

## 📊 COMPARISON TABLE

| Platform | Backend | Database | Free Tier | No CC | Auto-Deploy | Best For |
|----------|---------|----------|-----------|-------|-------------|----------|
| **Render** | ✅ | PostgreSQL ✅ | Yes | ✅ | ✅ | Backend |
| **Vercel** | ❌ | N/A | Yes | ✅ | ✅ | Frontend |
| **Netlify** | ❌ | N/A | Yes | ✅ | ✅ | Frontend |
| **Railway** | ✅ | PostgreSQL ✅ | Trial only | ✅ | ✅ | Backend (Paid) |
| **Heroku** | ✅ | PostgreSQL ✅ | ❌ Removed | ❌ | ✅ | Not recommended |
| **AWS** | ✅ | RDS ✅ | 1 year free | ❌ | Manual | Complex |

---

## 🚀 STEP-BY-STEP: Deploy on Render + Vercel (FREE)

### STEP 1: Deploy Backend to Render (10 minutes)

1. **Go to https://render.com**
2. **Click "Sign up"** - Sign in with GitHub
3. **Click "New +"** → **"Web Service"**
4. **Connect your GitHub repo:**
   - Select `Lonelyhackertechs/makpost`
   - Click "Connect"
5. **Configure:**
   - **Name:** `makpost-backend`
   - **Environment:** `Python 3`
   - **Build Command:** `cd webmak && pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command:** `cd webmak && gunicorn webmak.wsgi:application`
6. **Create Web Service** → Click "Create"

7. **Add PostgreSQL Database:**
   - Go to "Dashboard"
   - Click "+ New" → "PostgreSQL"
   - **Name:** `makpost-db`
   - **Region:** Same as backend
   - Click "Create Database"

8. **Connect Database to Backend:**
   - Go to backend service
   - Click "Environment"
   - Add these variables:
     ```
     DEBUG=False
     SECRET_KEY=your-secret-key-here
     ALLOWED_HOSTS=makpost-backend.onrender.com,yourdomain.com
     CORS_ALLOWED_ORIGINS=https://makpost.vercel.app,https://yourdomain.com
     DATABASE_URL=<Copy from PostgreSQL service page>
     ```

9. **Wait for deployment** (2-3 minutes)

10. **Get your backend URL:**
    - Example: `https://makpost-backend.onrender.com`
    - Save this - you'll need it for frontend

---

### STEP 2: Deploy Frontend to Vercel (3 minutes)

1. **Go to https://vercel.com**
2. **Click "Sign up"** - Sign in with GitHub
3. **Click "Add New"** → **"Project"**
4. **Import your repo:**
   - Find `makpost`
   - Click "Import"
5. **Configure:**
   - Framework: Vite (auto-detected)
   - Build Command: `npm run build` (auto-detected)
   - Output Directory: `dist` (auto-detected)

6. **Add Environment Variables:**
   - Click "Environment Variables"
   - Add:
     ```
     VITE_API_URL=https://makpost-backend.onrender.com
     VITE_API_BASE=/api
     ```

7. **Deploy!**
   - Click "Deploy"
   - Wait 1-2 minutes
   - Get your frontend URL: `https://makpost.vercel.app`

---

### STEP 3: Test Everything (5 minutes)

1. **Open your frontend:** `https://makpost.vercel.app`
2. **Try registering:**
   - Fill registration form
   - Click "Register"
3. **If you get CORS error:**
   - Go back to Render backend
   - Update `CORS_ALLOWED_ORIGINS` to include your Vercel URL
   - Redeploy
4. **Try creating a post** - if it works, you're done! ✅

---

## 🔧 RENDER.COM CONFIGURATION FILE

Create file: `render.yaml` in root of repo

```yaml
services:
  - type: web
    name: makpost-backend
    env: python
    plan: free
    buildCommand: cd webmak && pip install -r requirements.txt && python manage.py collectstatic --noinput
    startCommand: cd webmak && gunicorn webmak.wsgi:application
    envVars:
      - key: DEBUG
        value: "False"
      - key: PYTHON_VERSION
        value: "3.10"

  - type: pserv
    name: makpost-db
    plan: free
    ipAllowList: [] # allow all
```

---

## ⚠️ RENDER.COM IMPORTANT NOTES

### Free Tier Limitations
```
✅ 750 hours/month (about 1 service running 24/7)
✅ Unlimited databases
✅ Free SSL/HTTPS
✅ Auto-deploys from GitHub

⚠️ Spins down after 15 minutes of inactivity (takes 30s to wake up)
⚠️ Limited to 0.5 GB RAM
⚠️ Limited to 1 GB storage for database
```

### If Service Spins Down
- First request after 15 min inactivity = 30 second delay
- For class project: This is fine!
- For production: Upgrade to paid tier ($7/month)

---

## 🆓 OTHER FREE OPTIONS

### Option 2: Glitch.com
```
✅ Backend: YES (Node.js, but can use Python)
✅ Database: Free PostgreSQL
✅ No credit card needed
✅ Beginner-friendly
✅ Free tier: Limited RAM (512 MB)
⚠️ Less popular for production
```

### Option 3: PythonAnywhere
```
✅ Backend: Python hosting
✅ Database: MySQL available
✅ Free tier available
⚠️ Limited to 100 MB database
⚠️ Limited execution time
```

### Option 4: AWS (with free tier)
```
✅ Backend: EC2 (free for 12 months)
✅ Database: RDS (free for 12 months)
✅ Unlimited storage
⚠️ Complex setup
⚠️ Need credit card
⚠️ Easy to accidentally spend money
```

---

## ✅ RECOMMENDED: Render + Vercel Setup

### Why This Combination?
```
✅ Both completely free
✅ No credit card needed
✅ Perfect for class projects
✅ Professional appearance
✅ Easy to deploy
✅ GitHub integration
✅ Easy to upgrade later
```

### Architecture
```
┌─────────────────────────────────────┐
│        Your Vercel Frontend         │
│   https://makpost.vercel.app        │
└────────────────┬────────────────────┘
                 │
                 │ API Calls
                 │
┌────────────────▼────────────────────┐
│      Your Render Backend API        │
│  https://makpost-backend.onrender.com│
└────────────────┬────────────────────┘
                 │
                 │ SQL Queries
                 │
┌────────────────▼────────────────────┐
│     Render PostgreSQL Database      │
│          (Included FREE)            │
└─────────────────────────────────────┘
```

---

## 🎯 MIGRATION FROM RAILWAY TO RENDER

If you already have data on Railway:

1. **Export data from Railway:**
   ```bash
   railway run python manage.py dumpdata > data.json
   ```

2. **Push code to GitHub** (already done)

3. **Deploy to Render** (follow steps above)

4. **Load data in Render:**
   - Go to Render dashboard
   - Click backend service
   - Go to "Shell"
   ```bash
   python manage.py loaddata data.json
   ```

---

## 🔑 ENVIRONMENT VARIABLES FOR RENDER

### In Render Dashboard - Set These:

```bash
# Security
DEBUG=False
SECRET_KEY=<generate new one>

# Domains
ALLOWED_HOSTS=makpost-backend.onrender.com,yourdomain.com

# CORS (update with your Vercel URL)
CORS_ALLOWED_ORIGINS=https://makpost.vercel.app,https://yourdomain.com

# Database (Render auto-generates this)
DATABASE_URL=postgresql://...

# Frontend
FRONTEND_URL=https://makpost.vercel.app
```

---

## 📋 FINAL CHECKLIST

- ⬜ Sign up for Render.com (free, with GitHub)
- ⬜ Create PostgreSQL database on Render
- ⬜ Deploy backend to Render
- ⬜ Set environment variables on Render
- ⬜ Sign up for Vercel.com (free, with GitHub)
- ⬜ Deploy frontend to Vercel
- ⬜ Set VITE_API_URL in Vercel
- ⬜ Update CORS_ALLOWED_ORIGINS in Render
- ⬜ Test registration on frontend
- ⬜ Test creating a post
- ⬜ Check browser console (F12) for errors
- ⬜ Submit project to your teacher! 🎉

---

## 💰 COST COMPARISON

| Option | Backend | DB | Frontend | Total/Month | Notes |
|--------|---------|----|-----------|----|-------|
| **Render + Vercel** | Free | Free | Free | **$0** | ✅ Recommended |
| Glitch | Free | Free | Free | **$0** | Less popular |
| Railway | $5 | Included | Free | **$5+** | Paid |
| Heroku | Paid | Paid | Free | **$7+** | No free tier |
| AWS | Free 12mo | Free 12mo | Free | **$0-100+** | Risky for students |

---

## 🆘 TROUBLESHOOTING

### Backend URL shows error
```
1. Check Render logs: Dashboard → Service → Logs
2. Verify environment variables are set
3. Check DATABASE_URL is correct
4. Restart service: Dashboard → Manual Deploy
```

### CORS errors on frontend
```
1. Error: "Access-Control-Allow-Origin"
2. Go to Render backend
3. Add your Vercel URL to CORS_ALLOWED_ORIGINS
4. Restart deployment
```

### Database won't connect
```
1. Check Render PostgreSQL status
2. Verify DATABASE_URL is set
3. Check connection is from allowed IP
4. Restart backend service
```

### Service keeps spinning down
```
This is normal on free tier (after 15 min of inactivity)
Solution: Refresh page - it will wake up in 30 seconds
```

---

## 📞 SUPPORT

- **Render Help:** https://render.com/docs
- **Vercel Help:** https://vercel.com/docs
- **GitHub Issues:** Create issue in your repo

---

## 🎓 FOR YOUR TEACHER

If teacher asks about hosting:

```
✅ "I deployed on Render (free tier) and Vercel (free tier)"
✅ "Database: PostgreSQL on Render"
✅ "Frontend: React deployed on Vercel"
✅ "Both have automatic GitHub deployments"
✅ "All within free tier - no costs for student project"
```

---

## ✨ NEXT STEPS

1. **Right now:** Sign up for Render.com
2. **Next:** Follow deployment steps above
3. **Then:** Sign up for Vercel and deploy frontend
4. **Finally:** Test everything works

**Total time:** ~15 minutes  
**Cost:** $0  
**Result:** Live application ready to show! 🚀

---

**Good luck! You've got this! 💪**
