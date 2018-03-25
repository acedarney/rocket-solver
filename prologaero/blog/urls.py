from django.conf.urls import url, include
from django.urls import path
from .views import PostDetailView, PostListView, index

urlpatterns = [
    path('', index, name='blog-index'),
    url('posts/', PostListView.as_view(), name='blog'),
    url('post/<int:pk>/', PostDetailView.as_view(), name='post')
]
