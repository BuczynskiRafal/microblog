from django.urls import path
from .views import main_view
from .views import about
from .views import contact
from .views import user_profile

app_name = 'main'

urlpatterns = [
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('user/<int:user_id>/profile', user_profile, name='userprofile'),
    path('', main_view, name='main_view'),
]