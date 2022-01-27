import string
import random
from django.db import models
from django.utils.timezone import now
from django.utils.timezone import timedelta
from django.utils.text import slugify


def upload_to(instance, filename):
    return f"galleries/{instance.gallery.slug}/{filename}"


def get_random_text(n):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(n))


class CheckAgeMixin:

    def is_older_than_n_days(self, n=1):
        """Check if created is older than now() - n days"""
        delta = timedelta(days=n)
        return now() - self.created > delta


class Timestamped(models.Model, CheckAgeMixin):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    SLUG_BASE_FIELD = "title"
    SLUG_SUFFIX_LEN = 5
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    # def init(self, *args, kwargs):
    #     super().init(args, kwargs)
        # self.title = None

    def save(self, *args, kwargs):
        if self._state.adding and not self.slug:
            slug = slugify(getattr(self, self.SLUG_BASE_FIELD))
            slugs = self.__class__.objects.filter(slug=slug).values_list("slug", flat=True)
            if slugs:
                while True:
                    if slug in slugs:
                        slug += get_random_text(self.SLUG_SUFFIX_LEN)
                    else:
                        break
            self.slug = slug
        return super().save(*args, **kwargs)