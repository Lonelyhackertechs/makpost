# MakPost - React & Django Integration Guide

## Overview

MakPost is a university social connection platform with a Django REST API backend and React frontend. This guide will help you integrate and run both applications.

## Architecture

```
┌─────────────────┐         ┌──────────────────┐
│   React App     │◄─────►  │  Django API      │
│  (Port 5173)    │ HTTP    │  (Port 8000)     │
└─────────────────┘         └──────────────────┘
       UI                        Backend
```

## Prerequisites

- Python 3.10+
- Node.js 16+ and npm
- Git

## Backend Setup (Django)

### 1. Install Dependencies

```bash
cd webmak
pip install -r requirements.txt
```

If no `requirements.txt` exists, install these packages:

```bash
pip install django==5.2.6
pip install djangorestframework
pip install django-rest-framework-simplejwt
pip install django-cors-headers
pip install pillow  # For image uploads
```

### 2. Configure CORS

Update `webmak/webmak/settings.py`:

```python
INSTALLED_APPS = [
    # ... existing apps
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add at the beginning
    # ... other middleware
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",     # React development server
    "http://localhost:3000",      # Alternative port
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

# Allow credentials (cookies, authorization headers)
CORS_ALLOW_CREDENTIALS = True
```

### 3. Create Admin User and Migrate Database

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 4. Run Django Server

```bash
python manage.py runserver
```

The backend will run on: `http://localhost:8000`

## Frontend Setup (React)

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Edit `.env`:

```env
VITE_API_URL=http://localhost:8000
VITE_API_BASE=/api
```

### 3. Run React Development Server

```bash
npm run dev
```

The frontend will run on: `http://localhost:5173`

## Running Both Applications

### Terminal 1 - Backend

```bash
cd webmak
python manage.py runserver
```

### Terminal 2 - Frontend

```bash
cd frontend
npm run dev
```

Now open your browser and navigate to: `http://localhost:5173`

## Testing the Integration

### 1. Register a New User

- Go to `http://localhost:5173/register`
- Fill in the registration form
- Select your college
- Click "Register"

### 2. Login

- After registration, you'll be automatically logged in
- Or go to `http://localhost:5173/login`

### 3. Create a Post

- Click "Create Post" button
- Fill in the title and content
- Optionally add image/video
- Click "Create Post"

### 4. View Posts

- Your posts will appear in the Feed
- Click on a post to view details
- Add comments to posts

### 5. View User Profiles

- Click on any user's name to view their profile
- See all posts by that user

## API Endpoints Reference

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/makpost/register/` | Register new user |
| POST | `/makpost/login/` | Login user |
| POST | `/makpost/logout/` | Logout user |
| GET | `/makpost/my-profile/` | Get current user profile |
| GET | `/makpost/posts/` | List all posts (paginated) |
| GET | `/makpost/posts/<id>/` | Get post detail |
| POST | `/makpost/posts/` | Create new post |
| DELETE | `/makpost/posts/<id>/` | Delete post |
| GET | `/makpost/comments/` | List comments |
| POST | `/makpost/comments/` | Create comment |
| DELETE | `/makpost/comments/<id>/` | Delete comment |

## Authentication Flow

1. **Registration**: User provides email, password, name, and college
2. **Login**: User receives JWT access and refresh tokens
3. **Token Storage**: Tokens stored in localStorage
4. **API Requests**: All requests include Authorization header with access token
5. **Token Refresh**: When access token expires, refresh token is used to get new access token
6. **Logout**: Refresh token is blacklisted

## Troubleshooting

### CORS Errors

**Error**: "Access to XMLHttpRequest blocked by CORS policy"

**Solution**: 
- Ensure `django-cors-headers` is installed
- Check CORS settings in Django `settings.py`
- Verify `CORS_ALLOWED_ORIGINS` includes your frontend URL

### API Connection Error

**Error**: "Failed to connect to the API"

**Solution**:
- Make sure Django server is running on port 8000
- Check `VITE_API_URL` in `.env` matches your backend URL
- Check firewall settings

### 401 Unauthorized

**Error**: Getting 401 responses

**Solution**:
- Clear localStorage and login again
- Check if tokens are being properly stored
- Ensure JWT settings in Django are correct

### Database Errors

**Error**: "no such table" errors

**Solution**:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Profile Picture Not Uploading

**Error**: Images/videos not saving

**Solution**:
- Ensure `MEDIA_ROOT` and `MEDIA_URL` are configured in Django settings
- Check file upload size limits
- Verify media directory has write permissions

## Deployment

### Backend Deployment (Django)

1. Set `DEBUG = False` in `settings.py`
2. Add your domain to `ALLOWED_HOSTS`
3. Use a production server (Gunicorn)
4. Set up a database (PostgreSQL recommended)
5. Use environment variables for sensitive data

### Frontend Deployment (React)

1. Build the project:
   ```bash
   npm run build
   ```

2. Deploy `dist/` folder to:
   - Vercel
   - Netlify
   - GitHub Pages
   - Any static hosting

## Performance Tips

1. **Use pagination**: Already implemented for posts
2. **Lazy load images**: Consider implementing for post images
3. **Cache API responses**: Consider using React Query or SWR
4. **Optimize bundle**: Use code splitting for routes

## Next Steps

- Add real-time notifications with WebSockets
- Implement post search and filtering
- Add user follow/unfollow functionality
- Create admin dashboard
- Add email notifications
- Implement rate limiting

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review the API endpoints documentation
3. Check console logs for errors
4. Review Django logs for backend errors
