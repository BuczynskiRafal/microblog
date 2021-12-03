from django.shortcuts import render

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'list.html', {'posts':posts})


def post_details(request, post_id: int):
    detail= Post.objects.get(pk=post_id)
    return render(request, 'post_details.html', {'detail':detail})
