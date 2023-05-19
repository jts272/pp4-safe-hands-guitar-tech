from django.shortcuts import render
from django.views.generic import ListView

from .models import Service

# Create your views here.


class ServiceListView(ListView):
    """A simple, generic class-based view for presenting the list of
    services for the customer.

    Reference: https://docs.djangoproject.com/en/3.2/topics/class-based-views/generic-display/
    """
    model = Service
    # Specify template to use. Django looks for '<app>/<model>_list.html
    # by default with generic class-based views
    # Namespace convention is followed by dir named after the app within
    # the app's templates dir
    template_name = 'services/services.html'
    # A 'friendly' name to address the model in loops
    # Django defaults this to '<model>_list'
    # Alternatively, 'object_list' is always available to represent the
    # model in templates
    context_object_name = 'services'
