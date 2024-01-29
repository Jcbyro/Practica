from django.shortcuts import render

Tasks = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "Tasks/index.html", {
        "Tasks": Tasks
    })