from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_emp', views.create_emp, name='create_emp'),
    path('delete_emp/<int:emp_id>/', views.delete_emp, name='delete_emp'),
    path('edit_emp/<int:pk>/', views.edit_emp, name='edit_emp'),
    path('create_role', views.create_role, name='create_role'),
    path('delete_role/<int:r_id>/', views.delete_role, name='delete_role'),
    path('edit_role/<int:pk>/', views.edit_role, name='edit_role'),
    path('create_task', views.create_task, name='create_task'),
    path('delete_task/<int:t_id>/', views.delete_task, name='delete_task'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('tasks', views.tasks, name='tasks'),
    path('roles', views.roles, name='roles'),
]
