# CORS Configuration for React Integration

This guide explains how to properly configure CORS (Cross-Origin Resource Sharing) to allow your React frontend to communicate with the Django backend.

## What is CORS?

CORS is a security feature that prevents unauthorized cross-origin requests. Since your React app (running on port 5173) will make requests to your Django API (running on port 8000), you need to configure CORS.

## Step-by-Step Setup

### 1. Install django-cors-headers

```bash
pip install django-cors-headers
```

### 2. Update settings.py

Open `webmak/webmak/settings.py` and make the following changes:

#### Add to INSTALLED_APPS (at the beginning):

```python
INSTALLED_APPS = [
    'corsheaders',  # Add this at the top
    'django.contrib.admin',
    'django.contrib.auth',
    # ... rest of apps
]
```

#### Add to MIDDLEWARE (at the very beginning):

```python
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Must be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... rest of middleware
]
```

#### Add CORS Configuration:

Add these settings at the end of `settings.py`:

```python
# CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",     # React dev server
    "http://localhost:3000",      # Alternative port
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000",
]

# Allow credentials in CORS requests
CORS_ALLOW_CREDENTIALS = True

# Additional CORS settings
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
```

### 3. Update ALLOWED_HOSTS (Optional but Recommended)

```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '8000',  # or your server IP
]
```

### 4. Complete Settings Configuration

Your final JWT and REST Framework settings should look like this:

```python
# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

# JWT Configuration
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,
    
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JTI_CLAIM': 'jti',
    'TOKEN_TYPE_CLAIM': 'token_type',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
}
```

## Production Configuration

For production environments, update CORS settings:

```python
import os

# Production CORS Configuration
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
    "https://www.yourdomain.com",
    "https://api.yourdomain.com",
]

# Only allow credentials in production if necessary
CORS_ALLOW_CREDENTIALS = True

# Set DEBUG to False in production
DEBUG = False

# Update ALLOWED_HOSTS for production
ALLOWED_HOSTS = [
    'yourdomain.com',
    'www.yourdomain.com',
    'api.yourdomain.com',
]

# Use environment variables for sensitive data
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-insecure-key')
```

## Testing CORS

### Test with curl:

```bash
curl -H "Origin: http://localhost:5173" \
  -H "Access-Control-Request-Method: GET" \
  -H "Access-Control-Request-Headers: Content-Type" \
  -X OPTIONS http://localhost:8000/makpost/posts/
```

### Test with React:

After running `npm run dev`, try logging in. If CORS is configured correctly, you should:
- See successful API responses
- Not see CORS errors in browser console
- Be able to register, login, and create posts

## Common CORS Errors and Solutions

| Error | Cause | Solution |
|-------|-------|----------|
| "No 'Access-Control-Allow-Origin' header" | CORS not configured | Install and configure corsheaders |
| "Origin not allowed" | Frontend URL not in CORS_ALLOWED_ORIGINS | Add frontend URL to settings |
| "Credentials mode is 'include'" | CORS_ALLOW_CREDENTIALS not set | Set to True |
| "Method not allowed" | OPTIONS request blocked | Ensure corsheaders middleware is first |

## Environment Variables (Recommended)

Create a `.env` file in the Django project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
DATABASE_URL=sqlite:///db.sqlite3
```

Load in `settings.py`:

```python
import os
from pathlib import Path
from decouple import config

SECRET_KEY = config('SECRET_KEY', default='django-insecure-...')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost').split(',')
```

## Reference

- [Django CORS Headers Documentation](https://github.com/adamchainz/django-cors-headers)
- [CORS Explanation](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [Django Middleware Documentation](https://docs.djangoproject.com/en/5.2/topics/http/middleware/)