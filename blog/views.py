from django.shortcuts import render, get_object_or_404
# Utilize Django's generic class-based views
from django.views import generic, View
# Import the models that the views are based upon
from .models import Post
# Import the form required for posting comments
from .forms import CommentForm

# Create your views here.


class PostList(generic.ListView):
    """A generic class-based view that inherits from Django's built-in
    generic module.

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


class PostDetail(View):
    """A view that subclasses Django's base View. Displays the full
    detail of the given blog post.

    Reference: https://youtu.be/gUHXWF0M0c8
    """

    def get(self, request, slug, *args, **kwargs):
        # Get published posts
        queryset = Post.objects.filter(status=1)
        # Get the published post by slug
        post = get_object_or_404(queryset, slug=slug)
        # Get approved comments for the post, oldest first
        comments = post.comments.filter(approved=True).order_by('created_on')
        # Initialize like status as False
        liked = False
        # Set the like to true if the current user has liked the post
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Return request object, template and context object to use
        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked,
                'comment_form': CommentForm,
            }
        )
