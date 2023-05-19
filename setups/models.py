from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
# Create modifiable timestamps for setup dates
# Reference: https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.DateField.auto_now_add
from django.utils import timezone

# Create your models here.


class Setup(models.Model):
    """This model represents an instance of an instrument setup for a
    customer. The customer is represented by Django's stock User model.

    The specifics of the setup in question is linked by a 1:1 relation
    to an Instrument instance. Therefore, each Setup instance has a
    single, corresponding instrument instance related to it and vice
    versa.
    """
    # The customer refers to the stock Django user model
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    # Time and date the instrument was handed in for setup
    datetime_in = models.DateTimeField(default=timezone.now())
    # Time and date the instrument was returned to the customer
    datetime_out = models.DateTimeField(default=timezone.now())
    # Name of the instrument
    name = models.CharField(
        max_length=80, help_text='The name of the instrument')
    # Description of the work to be carried out for the customer
    description = models.TextField(
        help_text="Provide specific details of the customer's setup request")

    # Choices for setup completion status
    STATUS = (
        (0, 'Incomplete'), (1, 'Complete'), (2, 'Partially Complete'),
        (3, 'Awaiting Parts'),
    )

    status = models.IntegerField(choices=STATUS, default=0)

    # Methods of payment for the work done
    PAYMENT = (
        (0, 'Cash'), (1, 'Bank Transfer'), (2, 'PayPal'), (3, 'Other')
    )

    payment_method = models.IntegerField(choices=PAYMENT, default=0)

    def __str__(self):
        return f"{self.customer}'s {self.name} on {self.datetime_in}"


class Instrument(models.Model):
    """This model represents a customer's instrument that has been
    taken in for setup. Although a customer can have many instruments,
    each setup is unique. As such, each setup instance is linked with
    its own individual instrument."""
    # Create 1:1 link with the setup of the instrument
    job = models.OneToOneField(
        Setup, on_delete=models.CASCADE, primary_key=True)
    # Name of the instrument
    name = models.CharField(
        max_length=80, help_text='The name of the instrument')

    # Pre-setup fields

    # Images of the instrument
    pre_image_1 = CloudinaryField(null=True, blank=True)
    pre_image_2 = CloudinaryField(null=True, blank=True)
    pre_image_3 = CloudinaryField(null=True, blank=True)
    # String type
    pre_string_type = models.CharField(null=True, blank=True, max_length=80)
    # String gauges
    pre_string_1_gauge = models.IntegerField(null=True, blank=True)
    pre_string_2_gauge = models.IntegerField(null=True, blank=True)
    pre_string_3_gauge = models.IntegerField(null=True, blank=True)
    pre_string_4_gauge = models.IntegerField(null=True, blank=True)
    pre_string_5_gauge = models.IntegerField(null=True, blank=True)
    pre_string_6_gauge = models.IntegerField(null=True, blank=True)
    pre_string_7_gauge = models.IntegerField(null=True, blank=True)
    # Measurements
    pre_fret_height = models.CharField(null=True, blank=True, max_length=50)
    pre_fret_width = models.CharField(null=True, blank=True, max_length=50)
    pre_fretboard_radius = models.CharField(
        null=True, blank=True, max_length=50)
    pre_bridge_radius = models.CharField(null=True, blank=True, max_length=50)
    pre_neck_relief = models.CharField(null=True, blank=True, max_length=50)
    pre_action_1 = models.CharField(null=True, blank=True, max_length=50)
    pre_action_2 = models.CharField(null=True, blank=True, max_length=50)
    pre_action_3 = models.CharField(null=True, blank=True, max_length=50)
    pre_neck_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    pre_middle_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    pre_bridge_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    # Additional comments
    pre_comments = models.TextField(null=True, blank=True)

    # Post-setup fields

    # Images of the instrument
    post_image_1 = CloudinaryField(null=True, blank=True)
    post_image_2 = CloudinaryField(null=True, blank=True)
    post_image_3 = CloudinaryField(null=True, blank=True)
    # String type
    post_string_type = models.CharField(null=True, blank=True, max_length=80)
    # String gauges
    post_string_1_gauge = models.IntegerField(null=True, blank=True)
    post_string_2_gauge = models.IntegerField(null=True, blank=True)
    post_string_3_gauge = models.IntegerField(null=True, blank=True)
    post_string_4_gauge = models.IntegerField(null=True, blank=True)
    post_string_5_gauge = models.IntegerField(null=True, blank=True)
    post_string_6_gauge = models.IntegerField(null=True, blank=True)
    post_string_7_gauge = models.IntegerField(null=True, blank=True)
    # Measurements
    post_fret_height = models.CharField(null=True, blank=True, max_length=50)
    post_fret_width = models.CharField(null=True, blank=True, max_length=50)
    post_fretboard_radius = models.CharField(
        null=True, blank=True, max_length=50)
    post_bridge_radius = models.CharField(null=True, blank=True, max_length=50)
    post_neck_relief = models.CharField(null=True, blank=True, max_length=50)
    post_action_1 = models.CharField(null=True, blank=True, max_length=50)
    post_action_2 = models.CharField(null=True, blank=True, max_length=50)
    post_action_3 = models.CharField(null=True, blank=True, max_length=50)
    post_neck_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    post_middle_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    post_bridge_pickup_height = models.CharField(
        null=True, blank=True, max_length=50)
    # Additional comments
    post_comments = models.TextField(null=True, blank=True)

    # Represent the instrument as its own setup instance

    def __str__(self):
        return str(self.job)
