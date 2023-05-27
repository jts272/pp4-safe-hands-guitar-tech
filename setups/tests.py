from django.test import TestCase
from .models import Job
from django.utils import timezone
from django.contrib.auth.models import User

# Create your tests here.


class TestJobModel(TestCase):
    """Class to test the custom methods of the Job model."""

    def test_str_method(self):
        # Create a user for a job
        user = User(username='John')
        user.save()
        # Create a job with required fields for the string method
        job = Job.objects.create(
            user=user, instrument='Test instrument', date_in='2023-05-27')
        print(job)
        self.assertEqual(job.__str__(), (
            "John's Test instrument - booked in on 2023-05-27"))
