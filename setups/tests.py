from django.contrib.auth.models import User
from django.test import TestCase

from .models import Job

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
        self.assertEqual(job.__str__(), (
            "John's Test instrument - booked in on 2023-05-27"))

    def test_get_absolute_url(self):
        # Create a user for a job
        user = User(username='John')
        user.save()
        # Create a job with required fields
        job = Job.objects.create(
            user=user, instrument='Test instrument', date_in='2023-05-27')
        self.assertEqual(job.get_absolute_url(), '/jobs/1')
