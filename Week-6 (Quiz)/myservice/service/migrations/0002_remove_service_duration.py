# Generated by Django 5.0.7 on 2024-08-05 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='duration',
        ),
    ]
