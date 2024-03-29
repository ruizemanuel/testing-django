from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks":  request.session["tasks"]
    })

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST) # request.POST contiene la data que el usuario manda en el form
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {
                "form": form # si el formulario no es valido, returna el formulario con sus valores y el error correspondiente
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })
