# Generated by Django 5.1.1 on 2024-10-09 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_women_second_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='women',
            name='time_update',
        ),
    ]
