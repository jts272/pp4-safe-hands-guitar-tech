from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

# Create your views here.


def index(request):
    latest_blog_posts = Post.objects.order_by('-created_on')[:3]
    output = ', '.join([p.title for p in latest_blog_posts])
    return HttpResponse(output)
