from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.base import View

from .models import Book, RecordReader

class BooksView(View):
    """Список книг"""
    def get(self, request):
        books = Book.objects.all()
        record_take = RecordReader.objects.filter(existence=True)
        for i in books:
            for j in record_take:
                if i.id == j.book.id:
                    i.stock -= 1
                    
        return render(request, "books.html", {"books_list": books})



