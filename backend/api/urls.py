"""
URL Configuration for the API app

This file defines all the URL routes for the API endpoints.
"""

from django.urls import path
from . import views

# App name for namespacing (optional but recommended)
app_name = 'api'

urlpatterns = [
    # GET /api/facts/ - Retrieve all facts
    path('facts/', views.get_facts, name='get_facts'),
]
