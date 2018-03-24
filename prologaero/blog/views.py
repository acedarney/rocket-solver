from django.shortcuts import render
from django.views.generic import DetailView
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/header_footer.html')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
