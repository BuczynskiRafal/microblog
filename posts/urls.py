from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('<int:post_id>/', post_details, name='details'),
    path('<int:post_id>/edit/', edit_post, name='edit_post'),
    path('add/', add_post, name='add_post'),
    path('', post_list, name='list'),
]