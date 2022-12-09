from django.contrib import admin
from task_tracker.models import Task, Status, Type, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at', 'project']
    list_filter = ['status', 'project']
    search_fields = ['summary']
    exclude = []
    filter_horizontal = ['types']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'start_date', 'finish_date']
    list_filter = ['start_date', 'finish_date']
    search_fields = ['title', 'description']
    exclude = []


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
admin.site.register(Project, ProjectAdmin)
