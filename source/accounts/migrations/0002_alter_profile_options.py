# Generated by Django 4.1.3 on 2022-12-27 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': [('can_view_all_users', 'может просматривать всех пользователей на одной странице')], 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
