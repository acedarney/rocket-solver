from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'blog/header_footer.html')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    # TODO: Sort the blog posts in descending order
