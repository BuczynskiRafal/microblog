from django.shortcuts import render

from .models import Book


def all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_detail(request, book_id: int):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_detail.html', {'book': book})
