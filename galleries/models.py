import random
import string
from random import random
from django.db import models
from django.utils.text import slugify

from common.models import Timestamped


class Status(models.IntegerChoices):
    NEW = 1, 'new'
    HIDE = 2, 'hide'
    PUBLISHED = 3, 'published'


def upload_to(instance, filename):
    return f"galleries/{instance.gallery.slug}/{filename}"


def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


class Gallery(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=100)
    slug = models.SlugField()
    description = models.TextField(verbose_name="Opis", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Utworzono", auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(self.title)
            slugs = self.__class__.objects.filter(slug=slug).values_list('slug', flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_random_text(5)
                    else:
                        break
                self.slug = slug
        return super().save(*args, **kwargs)




class Photo(Timestamped):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    slug = models.SlugField()
    short_description = models.CharField(verbose_name="Któryki opis", max_length=300, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name="photos")
    created = models.DateTimeField(verbose_name="Utworzono", auto_now_add=True)
    modified = models.DateTimeField(verbose_name="Zmodyfikowano", auto_now=True)
    source = models.CharField(max_length=512, null=True, blank=True)
    status = models.PositiveIntegerField(choices=Status.choices, default=Status.NEW)

    def __str__(self):
        return self.slug

    @property
    def is_published(self):
        return self.status == Status.PUBLISHED

