from django.urls import path
from .views import *

app_name = 'galleries'

urlpatterns = [
    path("add/", add_gallery_view, name="add_gallery"),
    path('<int:gallery_id>/', gallery_details, name="gallery_details"),
    path('<int:gallery_id>/add/', add_photo_view, name="add_photo"),
    path('', galleries_list, name='galleries_list'),
]