from django.forms import ModelForm

from .models import Job


class JobModelForm(ModelForm):
    """This model form allows for finer tuning of the characteristics
    of the form that will be displayed in the generic editing views.

    Without providing this model form and its methods, the 'User'
    dropdown foreign key field will provide its entries in creation
    order. The __init___ method allows for finer sorting of the field's
    value order.
    """
    class Meta:
        model = Job
        fields = '__all__'

    # Order the dropdown fields for the 'User' field in the frontend
    # Reference: https://stackoverflow.com/questions/6062283/how-to-order-the-results-of-a-foreignkey-relationship-in-a-django-form
    def __init__(self, *args, **kwargs):
        super(JobModelForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = self.fields['user'].queryset.order_by(
            'username')
