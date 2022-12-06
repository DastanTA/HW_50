from django.contrib import admin
from django.urls import path
from task_tracker.views import MainPage, TaskView, CreateTask, UpdateTask, DeleteTask, ProjectMainPage, ProjectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectMainPage.as_view(), name='project_main'),
    path('project/<int:pk>', ProjectView.as_view(), name='view_project'),
    path('tasks/', MainPage.as_view(), name='main'),
    path('add/', CreateTask.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
