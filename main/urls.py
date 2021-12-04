from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('about', about, name='about'),
    path('', main_view, name='main_view'),
]