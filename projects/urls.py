# from django.urls import path
from django.urls.conf import path, include

from projects import views

urlpatterns = [

    path('', views.get_all_projects_list, name='project_list'),
    path('view/<int:pk>', views.project_view, name='project_view'),
    path('new', views.create_new_project, name='book_new'),
    path('edit/<int:pk>', views.update_existing_project, name='book_edit'),
    path('delete/<int:pk>', views.delete_existing_project, name='book_delete'),
    path('add', views.add_project, name='create_project'),
]
