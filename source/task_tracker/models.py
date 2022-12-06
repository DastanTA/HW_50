from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

from task_tracker.customvalidation import banned_words


class Status(models.Model):
    status_name = models.CharField(max_length=40, null=False, blank=False, verbose_name='название статуса')

    def __str__(self):
        return self.status_name


class Type(models.Model):
    type_name = models.CharField(max_length=40, null=False, blank=False, verbose_name='название типа')

    def __str__(self):
        return self.type_name


class Task(models.Model):
    summary = models.CharField(max_length=40, null=False, blank=False,
                               verbose_name='заголовок', validators=[banned_words, ])
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='описание',
                                   validators=[MinLengthValidator(10), ])
    status = models.ForeignKey(
        'task_tracker.Status', related_name='statuses',
        on_delete=models.RESTRICT, verbose_name='статус')
    types = models.ManyToManyField('task_tracker.Type', related_name='types', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время изменения')
    project = models.ForeignKey('task_tracker.Project', related_name='projects',
                                on_delete=models.CASCADE, verbose_name="проект", default=1)

    def __str__(self):
        return self.summary[:20]

    def get_absolute_url(self):
        return reverse('view_task', kwargs={'pk': self.pk})


class Project(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False, verbose_name="название",
                             validators=[banned_words, ], default='default title')
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='описание',
                                   validators=[MinLengthValidator(10), ], default='default description')
    start_date = models.DateField(verbose_name="дата начала", null=False, blank=False, default='2022-12-06')
    finish_date = models.DateField(verbose_name="дата окончания", null=True, blank=True)

    def __str__(self):
        return self.title[:15]

    def get_absolute_url(self):
        return reverse('view_project', kwargs={'pk': self.pk})