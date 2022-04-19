from django.urls import path
from lib import views

urlpatterns = [
    path("", views.BooksView.as_view())
]