from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=120)



class Project(models.Model):
  title = models.CharField(max_length=120)
  details = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  target = models.PositiveIntegerField()
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateTimeField()
  project_owner = models.ForeignKey(User, on_delete=models.CASCADE)



