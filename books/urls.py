from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path("<int:book_id>/", book_detail, name="book_detail"),
    path("<int:book_id>/borrows/", handle_book_borrows, name="borrows"),
    path('borrows-list/', handle_book_borrows, name='borrows_list'),
    path("add/", add_book, name="add"),
    path('', all_books, name='all_books'),
]