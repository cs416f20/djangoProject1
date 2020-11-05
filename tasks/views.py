from django.shortcuts import render

# Create your views here.

# global variable to store tasks
tasks = ['foo', 'bar', 'baz']

# this view renders some predefined tasks
def index(request):
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)


def add(request):
    # determine if the user is submitting a task via the form or just viewing the add task page
    # if the user is just viewing the add task page, else statement will render add.html page
    if request.method == 'POST':
        # get the entered task from the request
        task = request.POST.get('task')
        # add to the list (which is a global variable we created)
        tasks.append(task)
        # render the index page with the updated list of tasks
        return render(request, 'tasks/index.html', context={'tasks': tasks})
    else:
        return render(request, 'tasks/add.html')