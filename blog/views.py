from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.views import generic

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(status=1).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'