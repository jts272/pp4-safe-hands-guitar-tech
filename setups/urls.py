from django.urls import path

from . import views

app_name = 'setups'
urlpatterns = [
    # Job list view - shows a list of model entries
    path('', views.JobListView.as_view(), name='jobs'),
    # Job detail view - a single entry in full detail
    # The entry is accessed by capturing its primary key to pass on as
    # an argument for the class-based view
    # Class-based views always expect pk, not id
    # Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views#url_mapping_2
    path('<int:pk>', views.JobDetailView.as_view(), name='job_detail'),
    # URL configuration to CRUD-related class based views
    # Reference: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#url_configurations
    path('create/', views.JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/update/', views.JobUpdateView.as_view(),
         name='job_update'),
    path('<int:pk>/delete/', views.JobDeleteView.as_view(),
         name='job_delete'),

]
