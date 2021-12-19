from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('posts/<int:post_id>', post_details, name='details'),
    path('posts/add/', add_post, name='add_post'),
    path('posts/', post_list, name='list'),
]