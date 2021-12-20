from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from .models import Post
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published=True)
    q = request.GET.get('q')
    if q:
        posts = posts.filter(title__icontains=q)
    return render(request, 'list.html', {'posts': posts})


def post_details(request, post_id: int):
    detail = Post.objects.get(pk=post_id)
    context = {}
    if detail.published:
        context['detail'] = detail
    return render(request, 'post_details.html', context)


def add_post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            instance = post_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse("posts:add_post"))
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {'post_form': post_form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect(reverse("posts:add_post"))
    else:
        post_form = PostForm(instance=post)
    return render(request, 'main/add.html', {'post_form': post_form})
