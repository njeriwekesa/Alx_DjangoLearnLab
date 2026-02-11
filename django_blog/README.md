Django Blog Project

A fully functional Django blog application designed for learning and practicing web development with Django. This project includes user authentication, blog post management, comments, and basic template styling.

Project Overview

This Django blog project is designed as a learning exercise to understand:

Django project setup and app configuration

User authentication (registration, login, logout, profile management)

CRUD operations for blog posts

Template rendering and static file management

Secure handling of user data

Features

User registration, login, and logout

User profile view and editing

Blog post creation, reading, updating, and deletion (CRUD)

Commenting system for blog posts

Responsive templates using HTML, CSS, and JavaScript



Django Blog Authentication

This Django blog project includes a complete user authentication system, allowing users to register, log in, log out, and manage their profiles.

Features

User Registration: Sign up with a username, email, and password.

User Login: Authenticate with username and password.

User Logout: Securely log out and redirect to the login page.

Profile Management: View and edit your profile (username and email).

Routes / URLs
URL	Method	Description
/register/	GET, POST	User registration page and form submission
/login/	GET, POST	User login page and authentication
/logout/	POST	Logs out the user and redirects to login
/profile/	GET, POST	View and edit user profile details
How It Works
1. Registration

Visit /register/ to see the registration form.

Enter your username, email, and password.

Upon submission:

Django creates a new user in the database.

The user is automatically logged in.

Redirected to the profile page.

2. Login

Visit /login/ to see the login form.

Enter your username and password.

Upon successful login:

You are redirected to your profile page.

If credentials are invalid:

The form displays an error message.

3. Logout

Click the Logout button in the navigation bar.

This sends a POST request to /logout/.

Upon logout:

The user session is terminated.

You are redirected to /login/.


1. Profile Management

Visit /profile/ when logged in.

You can view and edit your username and email.

Submitting the form updates the database and reflects changes immediately.

Only logged-in users can access this page.

Testing Authentication

Register a new user

Go to /register/.

Fill out the form and submit.

Verify that you are logged in automatically and see your profile.

Log in

Go to /login/.

Enter valid credentials and submit.

Ensure you are redirected to the profile page.

Log out

Click the Logout button.

Confirm that you are redirected to /login/.

Try navigating to /profile/ — you should be redirected to login because you’re logged out.

Profile Editing

While logged in, go to /profile/.

Update username or email and submit.

Verify changes in the database and UI.

Notes / Security

All forms use CSRF tokens for security.

Passwords are securely hashed using Django’s built-in authentication system.

Logout uses a POST request to prevent CSRF attacks and unintended logouts.