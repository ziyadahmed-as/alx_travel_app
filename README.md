# Ovier views of ALX Travel App 
A scalable and modular Django-based web application for managing travel related listings. Built with RESTful APIs, Swagger documentation, and support for background task processing using Celery and RabbitMQ.

## 🚀 The Features Included to this projects 

- Modular Django architecture
- REST API with Django REST Framework
- MySQL database integration
- Secure environment variable handling with 'django-environ'
- CORS support for frontend-backend integration
- Auto-generated API documentation using Swagger (drf-yasg)
- Background task queuing setup with Celery & RabbitMQ (for future use)
- Production-ready configuration practices

## Heir the Technologies Used to develope the Travel Application 
- Python 3.x
- Django
- Django REST Framework (DRF)
- MySQL
- Celery & RabbitMQ (asynchronous task management)
- drf-yasg (Swagger API documentation)
- django-environ (secure .env handling)
- django-cors-headers

## 📁 Project Structure

alx_travel_app/
├── alxtravelapp/ 
│ ├── settings.py
│ ├── urls.py
│ └── celery.py
├── listings/ 
│ ├── models.py
│ ├── views.py
│ └── urls.py
├── .env 
├── manage.py
└── README.md