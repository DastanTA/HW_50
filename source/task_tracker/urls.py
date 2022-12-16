from django.urls import path
from task_tracker.views import \
    MainPage, TaskView, CreateTask, UpdateTask, DeleteTask, \
    ProjectMainPage, ProjectView, ProjectCreate, ProjectTaskCreateView, \
    ProjectUpdateView, ProjectDeleteView

app_name = 'task_tracker'

urlpatterns = [
    path('', ProjectMainPage.as_view(), name='project_main'),
    path('add_project/', ProjectCreate.as_view(), name='add_project'),
    path('project/<int:pk>', ProjectView.as_view(), name='view_project'),
    path('project/<int:pk>/update', ProjectUpdateView.as_view(), name='update_project'),
    path('project/<int:pk>/delete', ProjectDeleteView.as_view(), name='delete_project'),
    path('project/<int:pk>/add_task', ProjectTaskCreateView.as_view(), name='add_project_task'),
    path('tasks/', MainPage.as_view(), name='main'),
    path('add_task/', CreateTask.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='view_task'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
