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
