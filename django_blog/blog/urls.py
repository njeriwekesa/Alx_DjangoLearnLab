from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
  PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView, CommentCreateView, PostByTagListView
)
from . import views

urlpatterns = [
 #path("", views.home, name="home"),

  path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag'),
  path('search/', views.search_posts, name='search'),

  path('post/<int:pk>/comments/new/',CommentCreateView.as_view(),name='comment-create'),
  path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
  path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),

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