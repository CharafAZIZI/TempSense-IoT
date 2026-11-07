from django.urls import path
from . import views, api

urlpatterns = [
    path("api/get", api.Dlist, name='json'),
    path("api/post", api.Dhtviews.as_view(), name='json'),
    path('', views.dashboard, name='dashboard'),
]