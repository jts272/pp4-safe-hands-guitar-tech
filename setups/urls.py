from django.urls import path

from . import views

app_name = 'setups'
urlpatterns = [
    path('', views.JobListView.as_view(), name='jobs')
]
