# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path


# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<int:post_id>/', views.view_post, name='blog_post'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_blog_post/<int:post_id>',
         views.edit_blog_post, name='edit_blog_post'),
]
