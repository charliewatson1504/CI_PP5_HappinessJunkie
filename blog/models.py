# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from django.contrib.auth.models import User


# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """
    Model for blog posts
    """

    class Meta:
        ordering = ['-created_on']

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
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    body = models.TextField()
    created_on = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
