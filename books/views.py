from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

from .models import Book
from .models import Borrow
from .forms import BookForm
from .forms import BookBorrowForm


def all_books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def book_detail(request, book_id: int):
    book = Book.objects.get(pk=book_id)
    form = BookBorrowForm()
    form.helper.form_action = reverse("books:borrows", args=[book.id])
    return render(request, 'book_detail.html', {'book': book, 'form': form})


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add"))
    return render(request, 'add.html', {'form': form})


def handle_book_borrows(request, book_id):
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:
            if request.POST.get("borrow"):
                book = Book.objects.get(pk=book_id)
                Borrow.objects.create(user=user, book=book)
                book.available = False
                book.save()
    return HttpResponseRedirect(reverse("books:details", args=[book_id]))

