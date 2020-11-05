from django.urls import path
# Import the views file  . indicates the current directory
from . import views


# The `urlpatterns` list routes URLs to views.
urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add, name="add")
]