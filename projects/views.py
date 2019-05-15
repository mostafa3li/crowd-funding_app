from django.shortcuts import render

from .models import Project

from .forms import AddProjectForm

# Create your views here.

# @login_required
def index(request):
  return render(request, 'projects/index.html', {})

# @login_required
def add_project(request):
  if request.method == 'POST':
    my_form = AddProjectForm(request.POST)
    if my_form.is_valid():
      print(my_form.cleaned_data)
      Project.objects.create(**my_form.cleaned_data, project_owner=request.user)
    else:
      print(my_form.errors)
  else:
    my_form = AddProjectForm()
  return render(request, 'projects/add_project.html', {'form': my_form})