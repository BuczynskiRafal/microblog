from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path("books/<int:book_id>/", book_detail, name="book_detail"),
    path("books/<int:book_id>/borrows", handle_book_borrows, name="borrows"),
    path('books/borrows-list/', handle_book_borrows, name='borrows_list'),
    path("books/add", add_book, name="add"),
    path('books/', all_books, name='all_books'),
]