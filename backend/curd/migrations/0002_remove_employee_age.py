# Generated by Django 4.0.5 on 2022-08-31 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
    ]
