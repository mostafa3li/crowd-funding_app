from django.db import models
from django.contrib.auth.models import User


# Category Model
class Category(models.Model):
    title = models.CharField(max_length=120)


# Rate Model
class Rates(models.Model):
    rate = models.CharField(
        default=16,max_length=120
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Report Model
class Reports(models.Model):
    report = models.CharField(
        default=1,max_length=120
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# Image Model
class PImages(models.Model):
    image = models.ImageField(upload_to='project_images/', null=True)


# Donors Model
class Donors(models.Model):
    user = models.ForeignKey(User, related_name='donor', on_delete=models.CASCADE)
    donation = models.CharField(default=1,max_length=120)


# Project Model
class Project(models.Model):
    title = models.CharField(max_length=120)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    target = models.PositiveIntegerField(default=3)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    project_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    rates = models.ManyToManyField(Rates, related_name='rates')
    reports = models.ManyToManyField(Reports, related_name='reports')
    images = models.ManyToManyField(PImages, related_name='images')
    tags = models.ManyToManyField(Category, related_name='tags')
    donors = models.ManyToManyField(Donors, related_name='donors')
    total_rate = models.FloatField(default=0)
    total_reports = models.PositiveIntegerField(default=0)
    total_donation = models.PositiveIntegerField(default=0)
