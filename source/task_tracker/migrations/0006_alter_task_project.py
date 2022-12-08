# Generated by Django 4.1.3 on 2022-12-06 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0005_alter_project_description_alter_project_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='task_tracker.project', verbose_name='проект'),
        ),
    ]