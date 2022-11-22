from django.contrib import admin
from django.urls import path
from task_tracker.views import MainPage, TaskView, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainPage.as_view(), name='main'),
    path('add/', CreateTask.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('update/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
