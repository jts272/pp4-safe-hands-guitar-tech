# Import for redirection upon post liking
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
# Utilize Django's generic class-based views
from django.views import View, generic

# Import the form required for posting comments
from .forms import CommentForm
# Import the models that the views are based upon
from .models import Post

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
                # Bool to track that there is no pending post comment
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm,
            }
        )

    # HTTP post method handling for comment submission
    # Reference: https://youtu.be/K200vsthNQU
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        # Get the data from the posted form
        comment_form = CommentForm(data=request.POST)

        # Use Django's form validation
        if comment_form.is_valid():
            # Get poster's data for the model from the request object
            comment_form.instance.name = request.user.username
            comment_form.instance.email = request.user.email
            # Save the form, without submitting to the database
            comment = comment_form.save(commit=False)
            # Get the post that the comment was submitted to
            comment.post = post
            # Save now all data is collected
            comment.save()
        else:
            # Return empty form instance if not valid
            comment_form = CommentForm()

        # Return request object, template and context object to use
        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                # Set bool to mark pending status for post approval
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm,
            }
        )


class PostLike(generic.View):
    """This view handles the like functionality on blog posts."""

    def post(self, request, slug):
        # Get the post in question by slug
        post = get_object_or_404(Post, slug=slug)

        # Remove logged in user from post like field if present
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            # Add the current user to the like field
            post.likes.add(request.user)

        # Redirect to the current page
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
