# from django.urls import path
from django.urls.conf import path, include

from projects import views

urlpatterns = [

    path('', views.get_all_projects_list, name='project_list'),
    path('<int:pk>/view', views.project_view, name='view_project'),
    # path('new', views.create_new_project, name='book_new'),
    path('<int:pk>/update', views.update_existing_project, name='update_project'),
    path('<int:pk>/delete', views.delete_existing_project, name='delete_project'),
    path('add', views.add_project, name='create_project'),
]
