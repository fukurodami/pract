from django.contrib import admin

from . models import Author, Reader, Book, Genre, RecordReader

admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(RecordReader)