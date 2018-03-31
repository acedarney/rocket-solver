from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Post


# Create your views here.
def index(request):
    return render(request, 'blog/header_footer.html')


class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/post_detail.html'


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    # template_name = 'blog/post_list.html'
    # TODO: Sort the blog posts in descending order
