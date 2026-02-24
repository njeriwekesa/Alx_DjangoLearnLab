## Social Media API

A RESTful Social Media API built with Django and Django REST Framework (DRF).
This project implements user authentication using a custom user model and token-based authentication.

**Features**

- Custom User Model

- User Registration

- User Login

- Token Authentication (DRF)

- Profile-ready architecture

- Follower system (Many-to-Many self-reference)

**Tech Stack**

- Python

- Django

- Django REST Framework

- DRF Token Authentication

- PostgreSQL / SQLite (development)

**Setup Instructions**

 Install Django and Django REST Framework using pip, if not already installed: pip install django djangorestframework

Create a new Django project named social_media_api: django-admin startproject social_media_api

Navigate into your project directory and create a new Django app called accounts for handling user-related functionality: cd social_media_api python manage.py startapp accounts

Add 'rest_framework' and 'accounts' to the INSTALLED_APPS in settings.py.
Run Development Server
python manage.py runserver


Server runs at:

http://127.0.0.1:8000/

**Authentication System**

This project uses:

1. Custom User Model (extends AbstractUser)

2. Token Authentication (DRF)

3. Tokens are generated upon registration

**Custom User Model Overview**

Additional Fields for:
Field	Description
bio	Optional user biography
profile_picture	Optional profile image
followers	Self-referencing ManyToMany relationship

The followers field allows:

1. A user to follow other users

2. Asymmetrical relationships (symmetrical=False)

**API Endpoints**

Base URL:

http://127.0.0.1:8000/api/accounts/

- Register User

Endpoint:

POST /api/accounts/register/


**Design Decisions**

A custom user model was created at project start to allow future extensibility.

Token authentication was selected for simplicity and stateless API interactions.

Followers are implemented using a self-referencing ManyToMany field with symmetrical=False to allow directional relationships.

**Posts and Comments API Endpoints**

Authentication Required

Creating, updating, and deleting posts or comments requires authentication using Token Authentication.

Include the following header in your requests:

Authorization: Token your_token_here

You can obtain your token via the login endpoint: ```POST /api/accounts/login/```

- Post Endpoints

Base URL: ```/api/posts/```

1. List All Posts (Public)
```GET /api/posts/```

Supports pagination and search.

2. Retrieve Single Post (Public)
```GET /api/posts/<id>/```

Example:

```GET /api/posts/1/```

3. Create Post (Authenticated)
```POST /api/posts/```

Example Request:
``` json
{
  "title": "My First Post",
  "content": "This is my content."
}
```
4.  Update Post (Owner Only)
```PUT /api/posts/<id>/```

5. Delete Post (Owner Only)
```DELETE /api/posts/<id>/```

- Comment Endpoints

Base URL:```/api/comments/```

1. List All Comments
```GET /api/comments/```
2. Retrieve Single Comment
```GET /api/comments/<id>/```
3. Create Comment (Authenticated)
```POST /api/comments/```

Example Request:
``` json
{
  "post": 1,
  "content": "This is a comment."
}
```
4. Update Comment (Owner Only)
```PUT /api/comments/<id>/```
5. Delete Comment (Owner Only)
```DELETE /api/comments/<id>/```

**Search Functionality**

Posts support search by:

- title

- content

Example:

```GET /api/posts/?search=django```

This returns posts containing "django" in the title or content.

**Pagination**

Post and comment list endpoints use page-number pagination.

Example:

```GET /api/posts/?page=2```

Response format:
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/posts/?page=3",
  "previous": "http://127.0.0.1:8000/api/posts/?page=1",
  "results": [...]
}
```

**Permissions**

Anyone can view posts and comments.

Only authenticated users can create posts and comments.

## User Follow and Feed Functionality


The custom user model was updated to support following relationships:


following → Users that the current user follows

followers → Users that follow the current user (reverse relation)

symmetrical=False ensures follow relationships are directional

All follow and feed endpoints require Token Authentication.


Users can only modify their own follow relationships.

**What This Implements**

Social graph (user-to-user relationships)

Directional following

Personalized content feed

Secure token-based access control

## Likes Endpoints
Like a Post

```POST /posts/<id>/like/```

Response:
``` json
{
  "detail": "Post liked."
}
```
## Unlike a Post

```POST /posts/<id>/unlike/```

## Notifications Endpoint
Get Notifications

```GET /notifications/```

Returns:

- recipient
- actor
- verb
- target
- timestamp
- read

Notifications are ordered by most recent first.