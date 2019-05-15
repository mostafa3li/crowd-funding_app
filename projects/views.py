from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Project, Donors, Category, PImages, Reports, Rates, User

from .forms import AddProjectForm, ProjectModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title',
                  'details',
                  'category',
                  # 'start_date',
                  # 'end_date',
                  'images',
                  'project_owner',
                  'donors',
                  'rates',
                  'reports',
                  'tags',
                  'target',
                  'total_donation',
                  'total_rate',
                  'total_reports'
                  ]


# return all projects of all users
def get_all_projects_list(request):
    projects = list(Project.objects.all())
    data = {'projects': projects}
    return render(request, 'projects/list_projects.html', data)


# return specific project to view by Primary Key or ID
def project_view(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/show_project.html', {'project': project})

# create new project using form submitting
def add_project(request):
    if request.method == 'POST':
        my_form = AddProjectForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Project.objects.create(**my_form.cleaned_data, project_owner=request.user)
            return redirect('project_list')
        else:
            print(my_form.errors)
    else:
        my_form = AddProjectForm()
    return render(request, 'projects/create.html', {'form': my_form})

# update existing project
def update_existing_project(request, pk):
    project = Project.objects.get(pk=pk)
    my_form = ProjectModelForm(request.POST or None, instance=project)
    if my_form.is_valid():
        my_form.save()
        return redirect('project_list')
    context = {
        'form' : my_form
    }
    return render(request, 'projects/create.html',  context)

# def create_new_project(request):
#     project_data_form = ProjectForm(request.POST or None)
#     if project_data_form.is_valid():
#         project_data_form.save()
#         return redirect('project_list')
#     return render(request, 'projects/list_projects.html', {'project_data_form': project_data_form})


# delete existing project
def delete_existing_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/cancel_project.html', {'project': project})


def get_all_projects_user(request, user):
    projects = Project.objects.get(project_owner=user)
    return JsonResponse(projects, safe=True)


def get_all_projects_by_category(request, category):
    projects = Project.objects.get(category=category)
    return JsonResponse(projects, safe=True)


def get_one_project(request, primary_key, user):
    project = Project.objects.get(project_owner=user, pk=primary_key)
    return JsonResponse(project, safe=True)


def get_latest_projects_by_category(request, category):
    project_latest = Project.objects.last(category=category)
    return JsonResponse(project_latest, safe=True)

# def create_new_donation_on_project(request):
# def add_rate_on_project(request):
# def add_report_on_project(request):
# def upload_many_images_on_project(request):
# def search_by_title(request):
# def search_by_tag_or_category(request)
# form validation
# render views
