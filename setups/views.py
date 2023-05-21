from django.shortcuts import render
from django.urls import reverse_lazy
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
    """Displays the detailed breakdown of information for a given model
    record. The model is supplied to the class, which allows the
    '<model_name>_list.html' template to access model data."""
    model = Job


class JobCreateView(generic.CreateView):
    """Part of Django's suite of generic editing views. This is designed
    to facilitate the creation of records based on a model via a form.

    On submission of a valid form, this class' action is to get the
    absolute url of the model - to return to its detail page.

    Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#views
    """
    model = Job
    # Render all fields of the model in the data input form
    fields = '__all__'


class JobUpdateView(generic.UpdateView):
    """A generic view for updating models. Fields are prepopulated
    appropriately.

    Note that use of '__all__' will render any new fields added to the
    model.

    As with the Create view, this class looks for a template named
    '<model_name>_form.html', if not altered with the template_name_suffix
    attribute.

    Reference: https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#updateview
    """
    model = Job
    fields = '__all__'


class JobDeleteView(generic.DeleteView):
    """This view handles the deletion of the model record and as such,
    it does not require any form fields to be displayed.

    A success url is declared as Django has no obvious default for this.

    This view uses a template suffix name of '_confirm_delete' by default.

    Reference: https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#deleteview
    """
    model = Job
    # Redirect to the list view upon deletion of a record
    success_url = reverse_lazy('setups:jobs')
