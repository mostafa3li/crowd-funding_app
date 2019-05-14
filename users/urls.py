from .views import *
from django.urls import path
from django.conf.urls import url, include
urlpatterns = [
 path('login/',user_login,name='login'),
]