# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin


# Internal:
from .models import Post, Comment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class PostAdmin(admin.ModelAdmin):
    """
    Admin class for post model
    """
    list_display = (
        'title',
        'status',
        'created_on',
    )
    ordering = ('-created_on',)


class CommentAdmin(admin.ModelAdmin):
    """
    Admin class for comment model
    """
    list_display = (
        'user',
        'post',
        'created_on',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
