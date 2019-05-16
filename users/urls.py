from django.urls import path
from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('update/', views.update_profile, name='update_profile'),
    path('delete/', views.delete_profile, name='delete_profile'),
    path('view/', views.user_profile, name='user_profile'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    
]