# Generated by Django 4.1.3 on 2022-12-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0013_project_user_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
    ]
