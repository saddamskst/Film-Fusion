# Generated by Django 4.2.9 on 2024-04-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name': 'Clients Word'},
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Message',
            field=models.TextField(max_length=1200),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='Phone',
            field=models.IntegerField(max_length=200),
        ),
    ]