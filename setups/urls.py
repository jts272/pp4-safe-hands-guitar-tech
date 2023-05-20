from django.urls import path

from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='jobs')
]
