# Generated by Django 4.0.5 on 2023-05-06 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_student_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(null='Not Received', upload_to='pictures/'),
            preserve_default='Not Received',
        ),
    ]
