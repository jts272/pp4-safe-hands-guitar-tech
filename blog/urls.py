# Import the view  that the URLs route to
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog-detail')
]
