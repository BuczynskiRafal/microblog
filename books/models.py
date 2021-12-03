from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    publication_year = models.IntegerField()
    author = models.CharField(max_length=255)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | książka -> {self.title}"