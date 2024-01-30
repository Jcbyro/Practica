from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

# 1 Version
#Tasks = ["foo", "bar", "baz"]
# 2 Version
#Tasks = []

class NewTaskForm(forms.Form):
    Task = forms.CharField(label="New Task")
    #priority = forms.IntegerField(label="Priority", min_value=1, max_value= 10)

# Create your views here.
def index(request):
# 1 Version
#    return render(request, "Tasks/index.html", {
#        "Tasks": Tasks
#   })
# 2 Version
    # Check if there already exists a "Tasks" key in our session
    if "Tasks" not in request.session:
        # If not, create a new list
        request.session["Tasks"] = []

    return render(request, "Tasks/index.html", {
        "Tasks": request.session["Tasks"]
    })

def add(request):
    # Check if method is POST``
    if request.method == "POST":
        # Take in the data the user submitted and save it as form
        form = NewTaskForm(request.POST)
        
        # Check if form data is valid (server-side)
        if form.is_valid():
            # Isolate the Task from the 'cleaned' version of form data
            Task = form.cleaned_data["Task"]
            
            # Add the new Task to our list of tasks
#            Tasks.append(Task)
            
            # Add the new task to our list of tasks
            request.session["Tasks"] += [Task]
            
            # Redirect user to list of Tasks
            return HttpResponseRedirect(reverse("Tasks:index"))
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "Tasks/add.html", {
                "form": form
            })
            
    return render(request, "Tasks/add.html", {
        "form": NewTaskForm()
    })