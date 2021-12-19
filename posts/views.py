from django.shortcuts import render
from django.shortcuts import redirect

from .models import Post
from .form import PostForm


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
    if request.method == 'POST':
        post_form = PostForm(request.POST or None)
        if post_form.is_valid():
            post = post_form.save()
            return redirect(post_list)
        return render(request, 'add_post.html', {'post_form': post_form})
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {'post_form': post_form})

