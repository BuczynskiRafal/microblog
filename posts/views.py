from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def test(request):
    return HttpResponse(Post.objects.all())

