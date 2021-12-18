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
    author = models.ManyToManyField(Author, related_name="book")
    title = models.CharField(max_length=255)
    description = models.TextField()
    publication_year = models.IntegerField()
    author = models.CharField(max_length=255)
    available = models.BooleanField(default=True)
    tags = models.ManyToManyField("tags.Tag", related_name="books", blank=True)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | książka -> {self.title}"