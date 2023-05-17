from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from blog.models import Post

# Create your views here.


def index(request):
    latest_blog_posts = Post.objects.order_by('-created_on')[:3]
    template = loader.get_template('home/index.html')
    context = {
        'latest_blog_posts': latest_blog_posts
    }
    # output = ', '.join([p.title for p in latest_blog_posts])
    return HttpResponse(template.render(context, request))
