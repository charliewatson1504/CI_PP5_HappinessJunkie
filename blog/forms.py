# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms

# Internal:
from products.widgets import CustomClearableFileInput
from .models import Comment, Post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostForm(forms.ModelForm):
    """
    Class for post form
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'image',
            'blog_post_text'
        )

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    Class for comment form
    """

    class Meta:
        model = Comment
        fields = ('body')
