from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/new/', views.create_project, name='create_project'),
    path('projects/update/<int:project_id>/', views.update_project, name='update_project'),
    path('projects/delete/<int:project_id>/', views.delete_project, name='delete_project'),
    path('projects/<int:project_id>/tasks/new/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/status/', views.update_task_status, name='update_task_status'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name="logout"),
]
