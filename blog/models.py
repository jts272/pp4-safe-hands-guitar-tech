from django.db import models
# Use default Django User model
from django.contrib.auth.models import User
# Allow use of Cloudinary fields in the models
from cloudinary.models import CloudinaryField

# Create your models here.

# Tuple for draft/published blog post status
STATUS = ((0, 'Draft'), (1, 'Published'))


class Post(models.Model):
    """Table to store blog posts

    Reference: https://youtu.be/X7cdN0SQrX0
    """
    # Title of the blog post
    title = models.CharField(max_length=200, unique=True)
    # The slug is used for clean Django URLS
    slug = models.SlugField(max_length=200, unique=True)
    # A one-to-many relationship from the User model
    # Cascade ensures that if the 'one' is deleted, so to are associated
    # entries
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    # Date of post creation
    created_on = models.DateTimeField()
    # Date of post update
    updated_on = models.DateTimeField(auto_now=True)
    # The banner image associated with the current blog post
    # Has a default placeholder when none is specified
    featured_image = CloudinaryField('image', default='placeholder')
    # The text content of the blog post
    content = models.TextField()
    # The text viewable from paginated blog post display
    excerpt = models.TextField(blank=True)
    # The status of the blog post
    # Defaults to draft so that published status must be set manually
    status = models.IntegerField(choices=STATUS, default=0)
    # A many-to-many relationship is used as many users can like many
    # posts
    # Forms a list of Users which have liked the post in question
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        """Helper classes"""
        # Order posts by creation date, descending
        ordering = ['-created_on']

    # String representation of the object in human-readable form
    def __str__(self):
        return self.title

    # Return the number of likes the given post has
    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Table for comments, which are associated with blog posts

    Reference: https://youtu.be/X7cdN0SQrX0?t=336
    """
    # 1:n relationship to Post, which can have many comments
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    # Name of the commenter
    name = models.CharField(max_length=80)
    # Commenter's email address
    email = models.EmailField()
    # The body text of the comment
    body = models.TextField()
    # A timestamp for the creation of the post
    # Information on date field arguments:
    # https://docs.djangoproject.com/en/3.2/ref/models/fields/#datefield
    created_on = models.DateTimeField(auto_now_add=True)
    # A boolean to approve the post for display, set by site admin
    approved = models.BooleanField(default=False)

    class Meta:
        # Oldest posts first, in order to follow the conversation flow
        ordering = ['created_on']

    def __str__(self):
        # A string identifier for the comment and commenter
        return f"Comment {self.body} by {self.name}"
