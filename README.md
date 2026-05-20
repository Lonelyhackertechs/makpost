# MakPost - University Social Connection API

> A full-stack application designed to connect university students through a modern social platform.

[![Python](https://img.shields.io/badge/Backend-Python-blue?style=flat-square)](https://python.org)
[![Django](https://img.shields.io/badge/Framework-Django-green?style=flat-square)](https://djangoproject.com)
[![React](https://img.shields.io/badge/Frontend-React/Web-orange?style=flat-square)](https://reactjs.org)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**MakPost** is a university social connection platform that enables students to:
- Connect with peers on campus
- Share and discover posts
- Build community through social interactions
- Network with fellow students

This is a **full-stack application** combining a robust Python backend API with a modern web frontend.

---

## ✨ Features

### Backend API (`/src`)
- RESTful API for social interactions
- User authentication & authorization
- Post management system
- Service-oriented architecture
- Professional API documentation

### Frontend Application (`/webmak`)
- Django-based web interface
- Responsive design
- CORS-enabled for frontend-backend integration
- User-friendly navigation

---

## 🛠 Tech Stack

### Backend
- **Language**: Python
- **Framework**: Django/REST Framework
- **Architecture**: Service-based architecture

### Frontend
- **Type**: Django Web Application
- **Package Management**: npm
- **Features**: CORS integration, modular pages

### Development
- **Version Control**: Git & GitHub
- **API Integration**: RESTful endpoints with CORS support

---

## 📁 Project Structure

```
makpost/
├── src/                          # Backend API
│   ├── pages/                   # API endpoints & routes
│   └── services/                # Business logic & services
│
├── webmak/                       # Frontend Application
│   ├── makpost/                 # Django app
│   ├── webmak/                  # Django project settings
│   ├── manage.py               # Django CLI
│   └── .gitignore
│
├── package.json                 # Frontend dependencies
├── CORS_SETUP.md               # CORS configuration guide
├── INTEGRATION_GUIDE.md        # Frontend-Backend integration
└── README.md                   # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js & npm
- Git

### Backend Setup

```bash
# Navigate to backend directory
cd src

# Install dependencies
pip install -r requirements.txt

# Run the API server
python manage.py runserver
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd webmak

# Install dependencies
npm install

# Run Django development server
python manage.py runserver 8001
```

---

## 📡 API Documentation

For detailed API integration instructions, see [INTEGRATION_GUIDE.md](./INTEGRATION_GUIDE.md)

### CORS Configuration

The application supports Cross-Origin Resource Sharing (CORS) for secure frontend-backend communication.

For setup details, see [CORS_SETUP.md](./CORS_SETUP.md)

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000
```

---

## 🤝 Contributing

We welcome contributions! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 📧 Contact & Support

For questions, suggestions, or issues:
- Open an [GitHub Issue](https://github.com/Lonelyhackertechs/makpost/issues)
- Check existing documentation in [INTEGRATION_GUIDE.md](./INTEGRATION_GUIDE.md)

---

## 🎓 Project Status

✅ **Ready for Deployment**
- Backend API fully implemented
- Frontend integrated
- CORS configuration complete
- API documentation provided

---

**Last Updated**: May 2026 | **Repository Owner**: [Lonelyhackertechs](https://github.com/Lonelyhackertechs)
