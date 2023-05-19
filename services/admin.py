from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Service


class ServiceAdmin(SummernoteModelAdmin):
    """This class defines the appearance and functionality of the
    Service class in the admin panel."""
    # Fields to display in list view
    list_display = ('name', 'price')
    # Group the layout of the admin view
    fieldsets = (
        (
            'Service',
            {
                'fields': ('name', 'price', 'description')
            }
        ),
        # Keep image-related information together
        (
            'Images',
            {
                'fields': ('featured_image', 'featured_image_alt')
            }
        ),
    )
    # Specify the fields that require the WSYIWYG editor
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Service, ServiceAdmin)
