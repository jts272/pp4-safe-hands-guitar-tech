from django.test import TestCase
from .models import Service

# Create your tests here.


class TestModels(TestCase):
    """Coverage has shown that a test is required for the __str__
    method of the service model.

    Reference: https://youtu.be/o_CnAyqxyyo
    """

    def test_str_method(self):
        # Create a service and give it a name (price is required)
        service = Service.objects.create(name='Test Service', price=10)
        self.assertEqual(service.__str__(), 'Test Service')
