from django.shortcuts import render
from django.http import HttpResponse


# View functions are defined here

# This function takes request as a parameter and in turn returns an HttpResponse as the content of the page
# Each view you write is responsible for instantiating, populating, and returning an HttpResponse.
def hello(request):
    return HttpResponse("Hello, world!")


# This view method takes name as a parameter which is obtained from URL
# we create a context variable which is a dictionary consisting of key/value pairs
# the render function renders an HTML page with the information in the context variable
def greet(request, name):
    context = {
        'name': name.capitalize(),
        'last_name': 'Doe',
        'states': ['CT', 'MA', 'CA', 'HA'],
        'user_type': 'admin'
    }
    return render(request, 'hello.html', context)
