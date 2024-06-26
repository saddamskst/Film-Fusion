# Generated by Django 4.2.9 on 2024-04-08 15:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_Name', models.CharField(max_length=100)),
                ('Movie_Image', models.ImageField(upload_to='Movie_Image')),
                ('Year', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_year', message='Year must be a four-digit number.', regex='^\\d{4}$')])),
                ('Genre', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=1200)),
                ('Cast_Name', models.CharField(max_length=1200)),
                ('Directed_By', models.CharField(max_length=800)),
                ('rating', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Movie',
                'db_table': 'Movie_List',
            },
        ),
    ]
