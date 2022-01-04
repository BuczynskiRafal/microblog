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
    return render(request, "books.html", {"books": books})


def book_detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookBorrowForm()
    form.helper.form_action = reverse("books:borrows", args=[book.id])
    return render(request=request, template_name="book_detail.html", context={"book": book, "form": form})


def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("books:add"))
    return render(request, "add.html", {"form": form})


def handle_book_borrows(request, book_id=None):
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:
            if request.POST.get("borrow"):
                book = Book.objects.get(pk=book_id)
                Borrow.objects.create(user=user, book=book)
                book.available = False
                book.save()
                return HttpResponseRedirect(reverse("books:book_detail", args=[book_id]))
            else:
                keys = [key for key in request.POST.keys() if key.startswith("book_")]
                key = int(keys[0].split("_")[1])
                book = Book.objects.get(pk=key)
                borrow = Borrow.objects.filter(user=user, book=book).last()
                if not borrow.return_date:
                    borrow.return_date = timezone.now()
                    borrow.save()
                    book.available = True
                    book.save()
                return HttpResponseRedirect(reverse("books:borrows_list"))
    else:
        borrows = Borrow.objects.filter(user=user)
        return render(request, "borrows_list.html", {"borrows": borrows})
