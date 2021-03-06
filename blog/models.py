# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User
from stripe import Order

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Model for blog posts
    """

    title = models.CharField(
        max_length=250,
        unique=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    author = models.CharField(
        max_length=80
    )
    slug = models.SlugField(
        max_length=250,
        unique=True
    )
    image = models.ImageField(
        null=True,
        blank=True
    )
    blog_post_text = models.TextField()
    updated_on = models.DateTimeField(
        auto_now=True
    )
    created_on = models.DateField(
        auto_now_add=True
    )
    status = models.IntegerField(
        choices=STATUS,
        default=0
    )
    upvotes = models.ManyToManyField(
        User,
        related_name='blogpost_upvotes',
        blank=True,
        default=0
    )

    def __str__(self):
        return self.title

    def number_of_upvotes(self):
        return self.upvotes.count()


class Comment(models.Model):
    """
    Model for blog comments
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    name = models.CharField(
        max_length=80,
    )
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    approved = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
