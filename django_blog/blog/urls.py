from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)
from . import views

urlpatterns = [
 #path("", views.home, name="home"),

  path('', PostListView.as_view(), name='home'),  # Home page shows all posts
  path('post/', PostListView.as_view(), name='posts'),
  path('post/new/', PostCreateView.as_view(), name='post-create'),
  path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
  path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
  path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


  #Authentication
  path("register/", views.register, name="register"),
  path("profile/", views.profile, name="profile"),

  path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),

  path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]