from django.urls import path

from .views import TagAutocomplete

app_name = 'tags'

urlpatterns = [
    path('tag-autocomplete/', TagAutocomplete.as_view(create_field='name'), name="tag-autocomplete"),
]