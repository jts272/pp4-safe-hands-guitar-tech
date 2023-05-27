# Mixins for authentication of class-based views
# User must not only be logged in, but have the corresponding permission
# Reference: https://docs.djangoproject.com/en/3.2/topics/auth/default/#limiting-access-to-logged-in-users
from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import JobModelForm
from .models import Job

# Create your views here.


class JobListView(generic.ListView, PermissionRequiredMixin):
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
    # Test for permissions required as set in admin
    # Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#views
    permission_required = (
        'setups.can_create_job',
        'setups.can_update_job',
        'setups.can_delete_job')
    # Get entries that are visible to the public
    queryset = Job.objects.filter(public_status=1).order_by('-date_in')


class JobDetailView(generic.DetailView):
    """Displays the detailed breakdown of information for a given model
    record. The model is supplied to the class, which allows the
    '<model_name>_list.html' template to access model data."""
    model = Job


class JobCreateView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    generic.CreateView):
    """Part of Django's suite of generic editing views. This is designed
    to facilitate the creation of records based on a model via a form.

    On submission of a valid form, this class' action is to get the
    absolute url of the model - to return to its detail page.

    Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#views
    """
    # The form class to use from forms.py
    form_class = JobModelForm
    # The template to render from the app's templates folder
    template_name = 'setups/job_form.html'
    # Message to be displayed on job creation
    success_message = 'New job has been created!'

    # Test for permission to create
    # Reference: https://docs.djangoproject.com/en/3.2/topics/auth/default/#django.contrib.auth.mixins.UserPassesTestMixin
    def test_func(self):
        return self.request.user.has_perms('setups.can_create_job')


class JobUpdateView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    SuccessMessageMixin,
                    generic.UpdateView):
    """A generic view for updating models. Fields are prepopulated
    appropriately.

    Note that use of '__all__' will render any new fields added to the
    model.

    As with the Create view, this class looks for a template named
    '<model_name>_form.html', if not altered with the template_name_suffix
    attribute.

    Reference: https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#updateview
    """
    # The model to update
    model = Job
    form_class = JobModelForm
    template_name = 'setups/job_form.html'
    success_message = 'Your job has been updated!'

    # Test for permission to update
    def test_func(self):
        return self.request.user.has_perms('setups.can_create_job')


class JobDeleteView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    generic.DeleteView):
    """This view handles the deletion of the model record and as such,
    it does not require any form fields to be displayed.

    A success url is declared as Django has no obvious default for this.

    This view uses a template suffix name of '_confirm_delete' by default.

    Reference: https://docs.djangoproject.com/en/3.2/ref/class-based-views/generic-editing/#deleteview
    """
    model = Job
    # Redirect to the list view upon deletion of a record
    success_url = reverse_lazy('setups:jobs')
    success_message = 'Job has been deleted!'

    # Test for permission to delete
    def test_func(self):
        return self.request.user.has_perms('setups.can_delete_job')

    # Give message for deletion - cannot use mixin to hook to form_valid
    # Reference: https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(JobDeleteView, self).delete(request, *args, **kwargs)
