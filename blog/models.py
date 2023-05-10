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
