# from django.urls import path
from django.conf.urls import url, include

from .views import index, add_project

urlpatterns = [
  url('add', add_project),
  url('', index, name='index'),
]