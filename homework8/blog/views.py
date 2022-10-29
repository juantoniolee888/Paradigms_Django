from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.




def index(request):
    return HttpResponse("Hello, world!")

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.order_by('-pub_date')

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
