from django.db import models
from django.contrib.auth.models import User
from common.models import Timestamped


class Post(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    content = models.TextField(verbose_name="Treść")
    published = models.BooleanField(verbose_name="Opublikowany", default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    sponsored = models.BooleanField(verbose_name="Sponsorowany", default=False)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)
    tags = models.ManyToManyField('tags.Tag', related_name='posts')
    category = models.ManyToManyField('posts.Category', related_name='category', blank=True)
    file = models.FileField(upload_to='posts/image', null=True)
    image_field = models.ImageField(upload_to='post/images/%Y/%m/%d/', null=True, width_field='image_width')
    image_width = models.IntegerField(blank=True, null=True, editable=False)

    def __str__(self):
        return f"Klasa -> {self.__class__.__name__} | \n artykuł -> {self.title}"

    def __repr__(self):
        return f"{self.__class__.__name__} {self.title}"


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1024, null=True, blank=True)
