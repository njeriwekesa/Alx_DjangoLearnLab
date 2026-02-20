**Social Media API***

A RESTful Social Media API built with Django and Django REST Framework (DRF).
This project implements user authentication using a custom user model and token-based authentication.

🚀 **Features**

Custom User Model

User Registration

User Login

Token Authentication (DRF)

Profile-ready architecture

Follower system (Many-to-Many self-reference)

🛠* **Tech Stack**

Python

Django

Django REST Framework

DRF Token Authentication

PostgreSQL / SQLite (development)

⚙️ Setup Instructions

 Install Django and Django REST Framework using pip, if not already installed: pip install django djangorestframework

Create a new Django project named social_media_api: django-admin startproject social_media_api

Navigate into your project directory and create a new Django app called accounts for handling user-related functionality: cd social_media_api python manage.py startapp accounts

Add 'rest_framework' and 'accounts' to the INSTALLED_APPS in settings.py.
Run Development Server
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

🔐 Authentication System

This project uses:

Custom User Model (extends AbstractUser)

Token Authentication (DRF)

Tokens are generated upon registration

👤 Custom User Model Overview

Additional Fields for:
Field	Description
bio	Optional user biography
profile_picture	Optional profile image
followers	Self-referencing ManyToMany relationship

The followers field allows:

A user to follow other users

Asymmetrical relationships (symmetrical=False)

📡 API Endpoints

Base URL:

http://127.0.0.1:8000/api/accounts/

🔹 Register User

Endpoint:

POST /api/accounts/register/


🧠 Design Decisions

A custom user model was created at project start to allow future extensibility.

Token authentication was selected for simplicity and stateless API interactions.

Followers are implemented using a self-referencing ManyToMany field with symmetrical=False to allow directional relationships.