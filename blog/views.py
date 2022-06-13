# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render

# Internal:
from .models import Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def all_posts(request):
    """
    View for displaying list of blog posts
    """
    posts = Post.objects.filter(status=1).order_by('-created_on')

    template = 'blog/blog.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def homepage_post(request):
    """
    View for displaying latest post on index.html
    """
    post = Post.objects.filter(status=1)[0]

    template = 'home/index.html'
    context = {
        'post': = post,
    }

    return render(request, template, context)
