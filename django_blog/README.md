**Django Blog Project**

A fully functional Django blog application designed for learning and practicing web development with Django. This project includes user authentication, blog post management, comments, and basic template styling.

*Project Overview*

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



**Django Blog Authentication**

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


**Blog Post Management Features (CRUD)**

*Overview*

This update introduces full CRUD (Create, Read, Update, Delete) functionality for blog posts in the django_blog project. Authenticated users can create and manage their own posts, while all users can view published content.

The implementation uses Django class-based generic views with proper authentication and permission enforcement.

Features Implemented
1. List All Posts

URL: /posts/

View: ListView

Displays all blog posts.

Accessible to all users (authenticated and anonymous).

2. View Post Details

URL: /posts/<int:pk>/

View: DetailView

Displays full content of a single post.

Accessible to all users.

3. Create New Post

URL: /posts/new/

View: CreateView

Only authenticated users can create posts.

The author field is automatically set to the logged-in user.

Uses LoginRequiredMixin.

4. Update Post

URL: /posts/<int:pk>/edit/

View: UpdateView

Only the post author can edit.

Uses:

LoginRequiredMixin

UserPassesTestMixin

Enforces ownership via test_func().

5. Delete Post

URL: /posts/<int:pk>/delete/

View: DeleteView

Only the post author can delete.

Uses:

LoginRequiredMixin

UserPassesTestMixin

Permissions & Access Control

If a non-author attempts to edit or delete a post, the system returns:

403 Forbidden


This ensures backend-level security, not just UI restrictions.


*Testing*

The following were manually tested:

Public users can view posts and details.

Only authenticated users can create posts.

Only post authors can edit or delete posts.

Unauthorized edit/delete attempts return 403 Forbidden.

Navigation between views works correctly.


**Comment System Functionality**

*Overview*

This update enhances the django_blog project by introducing a fully functional comment system. Users can view comments on blog posts, while authenticated users can create, edit, and delete their own comments.

The comment system is integrated directly into each blog post’s detail page and follows strict authentication and authorization rules to ensure secure interaction.

Comment Model

A Comment model was created with the following fields:

post – ForeignKey to Post (many-to-one relationship)

author – ForeignKey to Django’s User

content – TextField for comment text

created_at – DateTimeField (auto-generated on creation)

updated_at – DateTimeField (auto-updated on modification)

Each comment belongs to a single blog post, and each post can have multiple comments.

Comment Features
1. View Comments

Comments are displayed on the blog post detail page.

All users (authenticated and anonymous) can view comments.

If no comments exist, a “No comments yet.” message is shown.

2. Add a Comment

Only authenticated users can add comments.

A comment form is displayed on the post detail page when logged in.

The author and post fields are automatically assigned in the backend.

After submission, the user is redirected back to the post detail page.

If a user is not authenticated, a login prompt is displayed instead of the form.

3. Edit a Comment

Only the comment’s author can edit their comment.

Edit links are conditionally displayed only to the comment author.

Backend protection is enforced using:

LoginRequiredMixin

UserPassesTestMixin

Unauthorized edit attempts result in:

403 Forbidden


After a successful update, the user is redirected to the related post detail page.

4. Delete a Comment

Only the comment’s author can delete their comment.

A confirmation page is displayed before deletion.

Backend protection ensures unauthorized users receive a 403 Forbidden response.

After deletion, users are redirected back to the associated post detail page.


Permissions & Access Control:

Security is enforced at the backend level using Django’s mixins. UI-level hiding of edit/delete buttons is only an additional convenience layer.


Testing Summary:

The following behaviors were verified:

Comments display correctly under each post.

Authenticated users can successfully add comments.

Comment authors can edit and delete their own comments.

Non-authors attempting to edit or delete receive a 403 Forbidden response.

Edit and delete options are not displayed for non-authors.

Navigation between post and comment views functions correctly.