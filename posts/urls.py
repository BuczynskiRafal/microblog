from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', post_list, name='post_list')
]