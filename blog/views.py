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
        else:
            messages.error(
                request, 'Post saving failed. Please check form is valid.'
            )
    else:
        form = PostForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_blog_post(request):
    """
    Allows editing of a blog post by a superuser
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies, only store owners can edit a post.')
        return redirect(reverse('blog'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Successfully edited the post')
            return redirect(reverse('blog_post', args=[post.id]))
        else:
            messages.error(
                request, 'Post saving failed. Please check form is valid.'
            )
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are updating {post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'post': post,
    }
    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """
    Deletes the blog post
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies, only store owners can delete a post.')
        return redirect(reverse('home'))

    product = get_object_or_404(Post, pk=postt_id)
    product.delete()
    messages.success(request, 'Post has been successfully removed!')

    return redirect(reverse('blog'))
