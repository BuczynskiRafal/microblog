from django.urls import path
from .views import *

urlpatterns = [
    path('books/', all_books, name='all_books')
]