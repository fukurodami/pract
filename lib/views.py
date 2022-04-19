from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View

from .models import Book, RecordReader

class BooksView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books.html", {"books_list": books})



