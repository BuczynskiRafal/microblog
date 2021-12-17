from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path("books/<int:book_id>/", book_detail, name="book_detail"),
    path('books/', all_books, name='all_books'),
]