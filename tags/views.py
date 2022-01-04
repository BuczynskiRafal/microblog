from django.shortcuts import render
from dal import autocomplete

from .models import Tag


class TagAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, request):
        if not self.request.user.is_authenticated:
            return Tag.objects.none()
        queryset = Tag.objects.all()
        if self.query:
            queryset = queryset.filter(name_istartswith=self.query)
        return queryset
