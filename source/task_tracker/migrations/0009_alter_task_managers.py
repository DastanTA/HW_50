# Generated by Django 4.1.3 on 2022-12-09 09:34

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0008_task_is_deleted'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='task',
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
