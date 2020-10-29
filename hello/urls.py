from django.urls import path
# Import the views file  . indicates the current directory
from . import views


# The `urlpatterns` list routes URLs to views.
urlpatterns = [
    path('', views.first_function),  # '' indicates nothing included after the localhost address, maps to first_function
]