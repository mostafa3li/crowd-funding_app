

from django.shortcuts import render
from django.http import HttpResponse
from . import views
from .forms.addcomment import AddCommentForm
from django.http import HttpResponseRedirect,HttpResponse
from .models import *
from projects.models import *
from users.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
@login_required(login_url='/#users/#login')

def AddComment(request,project_id):

    Project_Data = Project.objects.get(id=project_id)
    if request.method=='POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
        # Add New Commebnt in DB to database
            comment = form.save(commit=False)
            print(request.user)
            Project_Data = Project.objects.get(id=project_id)
            comment.user = request.user.userprofileinfo
            comment.project = Project_Data
            comment.save()
            return HttpResponse("Mission Complete")
        else:
             return HttpResponse("Mission Complete")
    else:

        form = AddCommentForm()
        comments={}
        comments = Comment.objects.filter(project=project_id)
        print(comments[0].title)
        return render(request, 'comments/index.html',{'form': form,'project_id':project_id,'comments':comments})
