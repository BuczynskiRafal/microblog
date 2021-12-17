from django.db import models
from django.utils.timezone import now
from django.utils.timezone import timedelta


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
