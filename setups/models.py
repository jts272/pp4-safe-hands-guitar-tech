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
    date_in = models.DateField(null=True, blank=True, help_text=(
        'Date format is YYYY-MM-DD'
    ), default=timezone.datetime.now)
    # Status of the job
    JOB_STATUS = ((0, 'Todo'), (1, 'In progress'), (2, 'Completed'))
    job_status = models.IntegerField(
        choices=JOB_STATUS, default=0, null=True, blank=True)
    # A description of the job required for the customer's instrument
    description = models.TextField(null=True, blank=True)
    # An image of the instrument
    image = CloudinaryField('image', null=True, blank=True)
    # Test if the listing is visible to the public
    PUBLIC_STATUS = ((0, 'Hidden'), (1, 'Visible'))
    public_status = models.IntegerField(
        choices=PUBLIC_STATUS, default=1, help_text=(
            'Select whether this job is visible to the public on the site'
        ))

    # Pre-setup specifications
    pre_string_brand = models.CharField(max_length=80, null=True, blank=True)
    pre_string_gauges = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide either the gauge of the set, e.g. 10-52 or each'
            ' individual string, from first string to last string'
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
    pre_notes = models.TextField(null=True, blank=True, help_text=(
        'Provide any additional notes before job completion if required'
    ))

    # Post-setup specifications
    post_string_brand = models.CharField(max_length=80, null=True, blank=True)
    post_string_gauges = models.CharField(
        max_length=80, null=True, blank=True, help_text=(
            'Provide either the gauge of the set, e.g. 10-52 or each'
            ' individual string, from first string to last string'
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
    post_notes = models.TextField(null=True, blank=True, help_text=(
        'Provide any additional notes after job completion'
    ))

    # Transactional information
    PAYMENT_METHOD = ((0, 'Cash'), (1, 'Bank Transfer'),
                      (2, 'PayPal'), (3, 'Other'))
    PAYMENT_STATUS = ((0, 'Unpaid'), (1, 'Paid'))
    payment_method = models.IntegerField(
        choices=PAYMENT_METHOD, default=0, null=True, blank=True)
    payment_status = models.IntegerField(
        choices=PAYMENT_STATUS, default=0, null=True, blank=True)
    # Date the instrument was returned to the customer
    date_out = models.DateField(null=True, blank=True, help_text=(
        'Date format is YYYY-MM-DD'
    ), default=timezone.datetime.now)

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
        return f"{self.user}'s {self.instrument} - booked in on {self.date_in}"

    def get_absolute_url(self):
        # Return to the detail page of the model instance
        # App namespace must be included if declared in the URLconf
        return reverse('setups:job_detail', args=[str(self.id)])
