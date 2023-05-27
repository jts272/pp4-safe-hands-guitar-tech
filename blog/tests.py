from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.


class TestPostModel(TestCase):
    """This class will test the methods of the Post model."""

    def test_str_method(self):
        # Create an author, which a post must have
        author = User(username='John')
        author.save()
        # Create a post with any required fields and a title to test
        post = Post.objects.create(
            created_on=timezone.now(), author=author, title='Test post')
        self.assertEqual(post.__str__(), 'Test post')
