from turtle import title
from django.db import models
from datetime import date

class Author(models.Model):
    """Автор книги"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=40)
    email = models.EmailField("Почта", null=True, unique=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Reader(models.Model):
    """Читатель книги"""
    first_name = models.CharField("Имя", max_length=30)
    last_name = models.CharField("Фамилия", max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

class Genre(models.Model):
    """Жанр книги"""
    genre = models.CharField("Жанр", max_length=100)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Book(models.Model):
    title = models.CharField("Название", max_length=100)
    genre = models.ForeignKey(Genre, verbose_name="Жанр", on_delete=models.SET_NULL, null=True)
    authors = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.SET_NULL, null=True)
    local_book = models.CharField("Геолокация", max_length=100)
    image = models.ImageField("Изображение", upload_to="books/")
    stock = models.PositiveIntegerField("Запас", default=1)
    

    def __str__(self):
        return f'{self.title}----Автор:{self.authors}'

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class RecordReader(models.Model):
    """Записи книги на руки"""
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.SET_NULL, null=True)
    reader = models.ForeignKey(Reader, verbose_name="Читатель", on_delete=models.SET_NULL, null=True)
    date = models.DateField("Дата взятия книги", default=date.today)
    existence = models.BooleanField("На руках")

    def __str__(self):
        return f'{self.reader} взял на руки {self.book} {self.date}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
