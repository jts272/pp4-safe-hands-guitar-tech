from django.shortcuts import render

from blog.models import Post

# Create your views here.


def index(request):
    # Get the five latest blog posts that are published
    latest_blog_posts = Post.objects.filter(
        status=1).order_by('-created_on')[:5]
    context = {'latest_blog_posts': latest_blog_posts}
    return render(request, 'home/index.html', context)
