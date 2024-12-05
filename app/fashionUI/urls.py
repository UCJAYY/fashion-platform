"""
This module contains all route and
view functions for the app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="base"),
]
