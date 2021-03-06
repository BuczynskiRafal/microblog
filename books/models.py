from django.db import models
from common.models import Timestamped


class Author(Timestamped):
    name = models.CharField(max_length=200)
    birth_year = models.IntegerField(blank=True, null=True)
    death_year = models.IntegerField(blank=True, null=True)
    biogram = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} <{self.birth_year}>"


class Book(Timestamped):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_year = models.IntegerField()
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField("tags.Tag", related_name="books", blank=True)
    authors = models.ManyToManyField(Author, related_name="books")
    cover = models.ImageField(upload_to="books/covers/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | książka -> {self.title}"


class Borrow(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="borrows")
    user = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="borrows"
    )
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
