# Generated by Django 4.1.3 on 2022-12-09 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0007_alter_task_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
