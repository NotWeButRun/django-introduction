from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book


# Create your views here.
class ListBookView(ListView):
    model = Book
    template_name = "book/book_list.html"

class DetailBookView(DetailView):
    model = Book
    template_name = "book/book_detail.html"
