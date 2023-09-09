from django.urls import path
from .views import ListBookView, DetailBookView, CreateBookView, DeleteBookView, UpdateBookView

urlpatterns = [
    path("book/", ListBookView.as_view(), name="list-book"),
    path("book/<int:pk>/detail/", DetailBookView.as_view(), name="detail-book"),
    path("book/create/", CreateBookView.as_view(), name="create-book"),
    path("book/<int:pk>/update/", UpdateBookView.as_view(), name="update-book"),
    path("book/<int:pk>/delete/", DeleteBookView.as_view(), name="delete-book"),
]