# Puddle---E-commerce-Platform-
Project Overview
Puddle is a Django-based e-commerce platform that allows users to buy and sell items. It includes features like user authentication, item listings, messaging, and a dashboard.

Features
Core Features
User authentication (login, signup, logout)
Item listing and browsing
Search functionality
User dashboard
Messaging system between users
Technical Stack
Backend: Django 5.2
Frontend: HTML, Tailwind CSS
Database: SQLite (default, can be configured for PostgreSQL/MySQL)
Static Files: Django static files
Media Storage: Local file system
puddle/
├── core/                    # Core app (main views, authentication)
├── items/                   # Items app (product listings)
├── Dashboard/               # User dashboard
├── conversation/            # Messaging system
├── puddle/                  # Project settings
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── manage.py                # Django management script
└── templates/               # Base templates
