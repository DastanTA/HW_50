from django.contrib import admin
from django.urls import path
from task_tracker.views import MainPage, TaskView, CreateTask, UpdateTask, DeleteTask, ProjectMainPage, ProjectView, ProjectCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectMainPage.as_view(), name='project_main'),
    path('add_project/', ProjectCreate.as_view(), name='add_project'),
    path('project/<int:pk>', ProjectView.as_view(), name='view_project'),
    path('tasks/', MainPage.as_view(), name='main'),
    path('add_task/', CreateTask.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
