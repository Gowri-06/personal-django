# Generated by Django 4.0.5 on 2022-08-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('age', models.IntegerField()),
                ('roll_no', models.IntegerField()),
                ('place', models.TextField()),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
