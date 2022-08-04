# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path


# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('manage_posts/', views.manage_blog_posts, name='manage_posts'),
    path('<int:post_id>/', views.view_post, name='blog_post'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_blog_post/<int:post_id>',
         views.edit_blog_post, name='edit_blog_post'),
    path('delete_blog_post/<int:post_id>',
         views.delete_blog_post, name='delete_blog_post'),
    path('delete_comment/<int:comment_id>',
         views.delete_comment, name='delete_comment'),
]
