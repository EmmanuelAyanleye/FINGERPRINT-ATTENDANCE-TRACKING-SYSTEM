# Generated by Django 5.1.6 on 2025-02-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.IntegerField(choices=[(100, '100 Level'), (200, '200 Level'), (300, '300 Level'), (400, '400 Level')]),
        ),
    ]
