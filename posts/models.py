from django.db import models
from django.contrib.auth.models import User
from common.models import Timestamped


class Post(Timestamped):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')
    category = models.ManyToManyField('posts.Category', related_name='category', blank=True)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | \n artykuł -> {self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1024, null=True, blank=True)
