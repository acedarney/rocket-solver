from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post
from .views import PostDetailView

urlpatterns = [
    url('', ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],
                             template_name='blog/blog.html'), name='blog'),
    url('<pk>/', PostDetailView.as_view(template_name='blog/post.html'), name='post')
]
