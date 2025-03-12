# 🚀 E-Commerce API with Django REST Framework
A complete e-commerce API built with Django REST Framework, featuring product management, order processing, and user authentication.

## 📚 Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Setup Instructions](#setup-instructions)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [Monitoring](#monitoring)
8. [Security](#security)
9. [API Documentation](#api-documentation)
10. [Contributing](#contributing)

## 📊 Project Overview
This project implements a full-featured e-commerce API with:
- Product management system
- Order processing
- User authentication
- Rate limiting
- Request monitoring
- API documentation

## 🎯 Features
- RESTful API endpoints
- JWT authentication
- Request throttling
- Product management
- Order processing
- User management
- API documentation
- Request monitoring
- Docker containerization

## 📦 Requirements
- Python 3.9+
- Docker
- Docker Compose
- Git

## 🚀 Setup Instructions
### 1. Clone Repository
```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

### 2. Create Environment File
```bash
cp .env.example .env
```

Update `.env` with your configuration:
```makefile
# Django Settings
SECRET_KEY=your_secure_key_here
DEBUG=False
ALLOWED_HOSTS=your_domain.com

# Database Settings
DATABASE_URL=mysql://user:password@localhost:3306/django-rsf

# Redis Settings
REDIS_URL=redis://localhost:6379/1
CELERY_BROKER_URL=redis://localhost:6379/1
CELERY_RESULT_BACKEND=redis://localhost:6379/1

# JWT Settings
ACCESS_TOKEN_LIFETIME=60  # minutes
REFRESH_TOKEN_LIFETIME=1440  # days
```

### 3. Build and Start Containers
```bash
# Build containers
docker-compose build

# Start containers in detached mode
docker-compose up -d
```

### 4. Initialize Database
```bash
# Create migrations
docker-compose exec api python manage.py makemigrations

# Apply migrations
docker-compose exec api python manage.py migrate
```

## 📊 Configuration
The project uses environment variables for configuration. The following variables are supported:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection URL
- `REDIS_URL`: Redis connection URL
- `CELERY_BROKER_URL`: Celery broker URL
- `CELERY_RESULT_BACKEND`: Celery result backend URL
- `ACCESS_TOKEN_LIFETIME`: JWT access token lifetime in minutes
- `REFRESH_TOKEN_LIFETIME`: JWT refresh token lifetime in days

## 🏃 Running the Application
### Development Mode
```bash
# Start containers
docker-compose up

# Start Celery worker
docker-compose exec api celery -A backend worker --loglevel=info

# Start Celery beat (for scheduled tasks)
docker-compose exec api celery -A backend beat --loglevel=info
```

### Production Mode
```bash
# Build and start containers in detached mode
docker-compose up --build -d
```

## 📊 Monitoring
The application provides several monitoring endpoints:

- **API Documentation**: `http://localhost:8000/docs/`
- **API Redoc**: `http://localhost:8000/redoc/`
- **Celery Flower**: `http://localhost:5555` (default credentials: `admin/admin`)
- **Django Admin**: `http://localhost:8000/admin/`
- **Silk Monitoring**: `http://localhost:8000/silk/`

## 🔒 Security
1. **Environment Variables**
- Store sensitive data in `.env` file
- Never commit `.env` to version control
- Use secure values in production

2. **JWT Authentication**
- Access tokens expire after 60 minutes
- Refresh tokens expire after 24 days
- Use HTTPS in production

3. **Rate Limiting**
- Anonymous users: 2 requests/minute
- Authenticated users: Configurable
- Endpoint-specific limits available

4. **Database Security**
- Use secure passwords
- Limit database access
- Regular backups

## 📚 API Documentation
The API documentation is available at `http://localhost:8000/docs/` and includes:

- API endpoints
- Request/response examples
- Authentication information
- Schema definitions

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Implement changes
4. Add tests
5. Submit pull request

## 📜 License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
