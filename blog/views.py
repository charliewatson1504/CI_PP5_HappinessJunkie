# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Internal:
from .models import Post
from .forms import CommentForm, PostForm
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


def manage_blog_posts(request):
    if not request.user.is_superuser:
        messages.error(request, 'Only store owners can view this page.')
        return redirect(reverse('blog'))

    posts = Post.objects.filter(status=0).order_by('-created_on')

    template = 'blog/manage_posts.html'
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def view_post(request, post_id):
    """
    View selected blog post
    """
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(blog_post=post_id).order_by('-created_on')
    number_of_comments = comments.count()

    comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.blog_post = post
            comment.user = request.user
            comment.save()

            messages.info(request, 'Comment submitted successfully')
            return redirect(reverse('blog_post', args=[post.id]))
        else:
            messages.error(
                request, 'Something went wrong with your comment submission, please try again')
            return redirect(reverse('blog_post', args=[post.id]))
    else:
        comment_form = CommentForm()

    template = 'blog/blog_post.html'
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
        'comment': comment,
        'number_of_comments': number_of_comments,
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
            post = form.save(commit=False)
            post.user = request.user
            post.author = request.user.username
            post.save()
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
def edit_blog_post(request, post_id):
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
def delete_blog_post(request, post_id):
    """
    Deletes the blog post
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Apologies, only store owners can delete a post.')
        return redirect(reverse('home'))

    product = get_object_or_404(Post, pk=post_id)
    product.delete()
    messages.success(request, 'Post has been successfully removed!')

    return redirect(reverse('blog'))
