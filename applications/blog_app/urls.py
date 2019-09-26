from django.urls import path, include

from applications.blog_app.views import HomeView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', HomeView, name='blog-home'),
    path('blog/<int:blog_id>', BlogDetailView, name='blog-detail'),
    path('create_blog', BlogCreateView, name='create-blog')
]

