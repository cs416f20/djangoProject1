from django.shortcuts import render
from django.http import HttpResponse


# View functions are defined here

# This function takes request as a parameter and in turn returns an HttpResponse as the content of the page
# Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
def first_function(request):
    return HttpResponse("Hello, world!")



