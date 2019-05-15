from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Project, Donors, Category, PImages, Reports, Rates, User


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
    return render(request, 'projects/list.html', data)


# return specific project to view by Primary Key or ID
def project_view(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/show.html', {'project': project})


# create new project using form submitting
def create_new_project(request):
    project_data_form = ProjectForm(request.POST or None)
    if project_data_form.is_valid():
        project_data_form.save()
        return redirect('project_list')
    return render(request, 'projects/list.html', {'project_data_form': project_data_form})


# update existing project
def update_existing_project(request, pk):
    project = Project.objects.get(pk=pk)
    project_form_data = ProjectForm(request.POST or None, instance=project)
    if project_form_data.is_valid():
        project_form_data.save()
        return redirect('project_list')
    return render(request, 'projects/list.html', {'project_form_data': project_form_data})


# delete existing project
def delete_existing_project(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/list.html', {'project': project})


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
