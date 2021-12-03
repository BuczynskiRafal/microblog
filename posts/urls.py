from django.urls import path
from .views import *

urlpatterns = [
    path('posts/<int:post_id>', post_details, name='post_detail'),
    path('posts/', post_list, name='post_list'),
]