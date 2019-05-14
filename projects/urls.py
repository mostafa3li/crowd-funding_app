from django.urls import path
from django.conf.urls import url, include

from .views import index

urlpatterns = [
  url('', index, name='index'),
  
 
]