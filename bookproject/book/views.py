from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, DeleteView, UpdateView
)
from .models import Book


# Create your views here.
class ListBookView(ListView):
    model = Book
    template_name = "book/book_list.html"

class DetailBookView(DetailView):
    model = Book
    template_name = "book/book_detail.html"

class CreateBookView(CreateView):
    model = Book
    template_name = "book/book_create.html"
    fields = ("title", "price", "category")
    success_url = reverse_lazy("list-book")

class DeleteBookView(DeleteView):
    model = Book
    template_name = "book/book_confirm_delete.html"
    success_url = reverse_lazy("list-book")

class UpdateBookView(UpdateView):
    model = Book
    template_name = "book/book_update.html"
    fields = ("title", "price", "category")
    success_url = reverse_lazy("list-book")