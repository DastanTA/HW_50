from django.db import models


class Status(models.Model):
    status_name = models.CharField(max_length=40, null=False, blank=False, verbose_name='название статуса')

    def __str__(self):
        return self.status_name


class Type(models.Model):
    type_name = models.CharField(max_length=40, null=False, blank=False, verbose_name='название типа')

    def __str__(self):
        return self.type_name


class Task(models.Model):
    summary = models.CharField(max_length=40, null=False, blank=False, verbose_name='заголовок')
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='описание')
    status = models.ForeignKey(
        'task_tracker.Status', related_name='statuses',
        on_delete=models.RESTRICT, verbose_name='статус')
    type = models.ForeignKey(
        'task_tracker.Type', related_name='типы',
        on_delete=models.RESTRICT, verbose_name='тип')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время изменения')

    def __str__(self):
        return self.summary[:20]
