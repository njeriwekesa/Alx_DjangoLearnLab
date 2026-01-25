from django.urls import path
from .views import login_view, book_list  

urlpatterns = [
    path("login/", login_view, name="login"),
    path("books/", book_list, name="book_list"),
]
