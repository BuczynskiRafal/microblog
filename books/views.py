from django.shortcuts import render

from .models import Book


def all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})
