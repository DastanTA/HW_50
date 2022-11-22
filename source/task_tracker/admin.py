from django.contrib import admin
from task_tracker.models import Task, Status, Type


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'type', 'created_at']
    list_filter = ['status', 'type']
    search_fields = ['summary']
    exclude = []


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_name']
    list_filter = ['status_name']
    search_fields = ['status_name']
    exclude = []


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']
    list_filter = ['type_name']
    search_fields = ['type_name']
    exclude = []


admin.site.register(Task, TaskAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Status, StatusAdmin)
