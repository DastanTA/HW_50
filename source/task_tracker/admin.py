from django.contrib import admin
from task_tracker.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['summary']
    exclude = []


admin.site.register(Task, TaskAdmin)
admin.site.register(Type)
admin.site.register(Status)
