from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | \n artykuł -> {self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.title}"
