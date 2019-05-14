from django.db import models
from django.contrib.auth.models import User
from projects import models as Project_Application


# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=120)
    project = models.ForeignKey(Project_Application.Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
