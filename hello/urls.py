from django.urls import path
# Import the views file  . indicates the current directory
from . import views


# The `urlpatterns` list routes URLs to views.
urlpatterns = [
    path('<str:name>', views.greet), # this routes expects a string in the URL so the user has to provide some text in the url like /hello/john
]