from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from .models import Comment, Post

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

    def test_number_of_likes(self):
        # Create an author, which a post must have
        author = User(username='John')
        author.save()
        # Create an reader to like the post
        reader = User(username='Jill')
        reader.save()
        # Create a post with any required fields and a title to test
        post = Post.objects.create(
            created_on=timezone.now(), author=author, title='Test post')
        # Add the author and reader to the n:n likes field
        post.likes.set([author, reader])
        self.assertEqual(post.number_of_likes(), 2)

    def test_number_of_approved_comments(self):
        # Create an author, which a post must have
        author = User(username='John')
        author.save()
        # Create a post with any required fields and a title to test
        post = Post.objects.create(
            created_on=timezone.now(), author=author, title='Test post')
        # Create a comment, which is not approved by default
        comment = Comment.objects.create(post=post, body='Test comment')
        comment.save()
        # Create a comment that is approved
        approved_comment = Comment.objects.create(
            post=post, body='Approved comment', approved=True)
        approved_comment.save()
        # There should only be one approved comment out of two
        self.assertEqual(post.number_of_approved_comments(), 1)


class TestCommentModel(TestCase):
    """This tests the Comment model, for which there is a string method."""

    def test_str_method(self):
        # Create an author, which a post must have
        author = User(username='John')
        author.save()
        # Create a post to be commented on
        post = Post.objects.create(
            created_on=timezone.now(), author=author, title='Test post')
        # Create an reader to make a comment
        reader = User(username='Jill')
        reader.save()
        # Create a comment with some body text
        comment = Comment.objects.create(
            post=post, body='Test comment', name=str(reader))
        comment.save()
        self.assertEqual(comment.__str__(), 'Comment Test comment by Jill')
