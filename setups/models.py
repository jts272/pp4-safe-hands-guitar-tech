from datetime import date

from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create modifiable timestamps for setup dates
# Reference: https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.DateField.auto_now_add
from django.utils import timezone

# Create your models here.


class Job(models.Model):
    """This model represents a job that is performed for a registered
    user's instrument."""
    # Related to a site member from Django's built-in User model
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    # The user's instrument that the job will be performed on
    # Cannot be blank as a job must have an associated instrument
    instrument = models.CharField(max_length=80)
    # Date the instrument was taken in for service
    date_in = models.DateField(default=timezone.now, null=True, blank=True)
    # Status of the job
    JOB_STATUS = ((0, 'Todo'), (1, 'In progress'), (2, 'Completed'))
    job_status = models.IntegerField(
        choices=JOB_STATUS, default=0, null=True, blank=True)
    # A description of the job required for the customer's instrument
    description = models.TextField(null=True, blank=True)
    # An image of the instrument
    image = CloudinaryField('image', null=True, blank=True)

    # Pre-setup specifications
    pre_string_brand = models.CharField(max_length=80, null=True, blank=True)
    pre_string_gauges = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide either the gauge of the set, e.g. 10-52 or each'
            '  individual string, from first string to last string'
        ))
    pre_scale_length = models.CharField(max_length=80, null=True, blank=True)
    pre_fretboard_radius = models.CharField(
        max_length=80, null=True, blank=True)
    pre_bridge_saddle_radius = models.CharField(
        max_length=80, null=True, blank=True)
    pre_fret_width_and_height = models.CharField(
        max_length=80, null=True, blank=True)
    pre_neck_relief = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    pre_nut_action = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify if the reading is open or fretted'
        ))
    pre_action_1 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    pre_action_2 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    pre_action_3 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    pre_neck_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )
    pre_middle_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )
    pre_bridge_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )

    # Post-setup specifications
    post_string_brand = models.CharField(max_length=80, null=True, blank=True)
    post_string_gauges = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide either the gauge of the set, e.g. 10-52 or each'
            '  individual string, from first string to last string'
        ))
    post_scale_length = models.CharField(max_length=80, null=True, blank=True)
    post_fretboard_radius = models.CharField(
        max_length=80, null=True, blank=True)
    post_bridge_saddle_radius = models.CharField(
        max_length=80, null=True, blank=True)
    post_fret_width_and_height = models.CharField(
        max_length=80, null=True, blank=True)
    post_neck_relief = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    post_nut_action = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify if the reading is open or fretted'
        ))
    post_action_1 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    post_action_2 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    post_action_3 = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Specify at which fret the measurement was taken'
        ))
    post_neck_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )
    post_middle_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )
    post_bridge_pickup_height = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide values for polepiece height on bass and treble side, with'
            ' the last fret fretted'
        )
    )

    # Transactional information
    PAYMENT_METHOD = ((0, 'Cash'), (1, 'Bank Transfer'),
                      (2, 'PayPal'), (3, 'Other'))
    PAYMENT_STATUS = ((0, 'Unpaid'), (1, 'Paid'))
    payment_method = models.IntegerField(
        choices=PAYMENT_METHOD, default=0, null=True, blank=True)
    payment_status = models.IntegerField(
        choices=PAYMENT_STATUS, default=0, null=True, blank=True)
    # Date the instrument was returned to the customer
    date_out = models.DateField(default=timezone.now, null=True, blank=True)

    class Meta:
        # Newest entries shown first
        ordering = ['-date_in']
        # Permissions for delegating model CRUD functionality
        # Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#permissions
        permissions = (
            ('can_create_job', 'Create a job'),
            ('can_update_job', 'Update a job'),
            ('can_delete_job', 'Delete a job'),
        )

    def __str__(self):
        return f"{self.user}'s {self.instrument} - Booked in on {self.date_in}"

    def get_absolute_url(self):
        # Return to the detail page of the model instance
        # App namespace must be included if declared in the URLconf
        return reverse('setups:job_detail', args=[str(self.id)])


# --------------------------------------------------------------------------- #


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


# --------------------------------------------------------------------------- #


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    details = models.TextField()
    related_order = models.ForeignKey(
        'Order', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Product {self.id}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    related_product = models.ForeignKey(
        Product, on_delete=models.CASCADE, null=True)
    date_in = models.DateField(default=timezone.now)
    date_out = models.DateField(default=timezone.now)
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

    amount_paid = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id}"
