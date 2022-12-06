# Generated by Django 4.1.3 on 2022-12-05 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0003_project_alter_task_description_alter_task_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='task_tracker.project', verbose_name='проект'),
        ),
    ]