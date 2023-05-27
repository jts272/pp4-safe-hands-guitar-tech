from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """Tests for the home app, whose only view renders the homepage,
    with recent blog posts.

    Reference: https://youtu.be/cppD3NQJXb8
    """

    def test_get_homepage(self):
        # Get the URL HTTP response code and template
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
