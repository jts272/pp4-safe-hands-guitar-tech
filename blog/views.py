from django.shortcuts import render
# Utilize Django's generic class-based views
from django.views import generic
# Import the models that the views are based upon
from .models import Post

# Create your views here.


class PostList(generic.ListView):
    """A generic class-based view that inherits from Django's built-in
    generic module

    Reference: https://youtu.be/LP-glKOWpi8
    """
    # The model this class will use
    model = Post
    # Get published posts, newest first
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    # The HTML page that the view will render
    template_name = 'blog.html'
    # Set the maximum number of posts to appear on one page
    # Navigation will be added automatically when the number is exceeded
    paginate_by = 4
