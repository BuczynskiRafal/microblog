from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Book
from .models import Author
from .models import Borrow


class BookResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    exclude = ['authors']
    list_display = ['id', 'title', 'available']
    search_fields = ['title', 'description', 'author']
    list_filter = ['available',]
    autocomplete_fields = ['tags']
    resource_class = BookResource


class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'birth_year', 'death_year', 'biogram']
    search_fields = ['name', 'birth_year',]
    list_filter = ['name',]
    resource_class = AuthorResource


class BookBorrowResource(resources.ModelResource):
    class Meta:
        model = Book


@admin.register(Borrow)
class BookBorrowAdmin(ImportExportModelAdmin):
    list_display = ['book', 'user', 'borrow_date', 'return_date']
    search_fields = ['book', 'user',]
    list_filter = ['borrow_date',]
    resource_class = BookBorrowResource
