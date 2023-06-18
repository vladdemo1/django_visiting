""" This module contains main end-points for this app """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name="api-overview"),
]
