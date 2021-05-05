from django.shortcuts import render

from apps.posts.models import Post


def index(request):
    posts = Post.objects.all()  # select * from post
    return render(request=request, template_name='pages/index.html', context={'posts': posts} )