from django.db import models
from django.contrib.auth.models import User
from projects import models as Project_Application
from users.models import *



# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=120)
    project = models.ForeignKey(Project_Application.Project, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
