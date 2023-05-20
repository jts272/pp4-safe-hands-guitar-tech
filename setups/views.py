from django.shortcuts import render
from django.views import generic
from .models import Job

# Create your views here.


class JobListView(generic.ListView):
    """Generic list view to display jobs in the database.

    This generic class-based view will be looking for the following path:
    '/<app_name>/templates/<app_name>/<model_name>_list.html' as its
    template, unless specified.

    The context object name to be used in template loops defaults to:
    '<lowercase_model_name>_list'

    The queryset can be overridden if required my adding a get_queryset
    method, which uses the QuerySet API syntax (dunders) to filter.

    Reference: 
    https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views#view_class-based
    https://docs.djangoproject.com/en/3.2/topics/db/queries/#field-lookups
    """
    model = Job


class JobDetailView(generic.DetailView):
    model = Job
