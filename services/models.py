from cloudinary.models import CloudinaryField
from django.db import models


# Create your models here.
class Service(models.Model):
    """This model represents the services that customers can choose from
    along with their corresponding prices."""
    # Name of the service to be carried out
    name = models.CharField(max_length=80)
    # Price of the service, with no upper limit or fractional digits
    price = models.DecimalField(max_digits=4, decimal_places=0)
    # An overview of the work to be done in more detail
    description = models.TextField()
    # An image to associate with the service
    featured_image = CloudinaryField('image')
    # An image description for assistive technologies
    featured_image_alt = models.TextField(
        help_text=(
            'Provide a text description of the featured image for assistive'
            ' technologies'
        ))

    # Order by price, lowest first, when querying the model
    class Meta:
        ordering = ['-price']

    def __str__(self):
        """String representation of an instance of this object."""
        return self.name
