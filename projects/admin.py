from django.contrib import admin

from .models import Category, Project,Rates,Reports,PImages,Donors

# Register your models here.

admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Rates)
admin.site.register(Reports)
admin.site.register(PImages)
admin.site.register(Donors)