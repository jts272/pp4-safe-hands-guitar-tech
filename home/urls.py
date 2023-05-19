from django.urls import path

from . import views

# Specify app_name to namespace this app's URLs for use site-wide
app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]
