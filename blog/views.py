# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Internal:
from .models import Post, Comment
from .forms import PostForm
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


def view_post(request, post_id):
    """
    View selected blog post
    """
    post = get_object_or_404(Post, pk=post_id)

    template = 'blog/blog_post.html'
    context = {
        'post': post,
    }

    return render(request, template, context)


@login_required
def add_blog_post(request):
    """
    Add a new blog post
    """
    if not request.user.is_superuser:
        messages.error(request, 'Apologies, only store owners can add a post.')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully created post')
            return redirect(reverse('blog_post', args=[post.id]))
