from django.urls import path
from .views import ListBookView, DetailBookView

urlpatterns = [
    path("book/", ListBookView.as_view()),
    path("book/<int:pk>/detail/", DetailBookView.as_view()),
]