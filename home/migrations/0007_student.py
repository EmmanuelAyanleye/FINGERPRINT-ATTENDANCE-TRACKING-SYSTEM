# Generated by Django 5.1.6 on 2025-02-28 01:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_course_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('matric_number', models.CharField(max_length=20, unique=True)),
                ('session', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('department', models.CharField(max_length=100)),
                ('level', models.IntegerField(choices=[(100, '100 Level'), (200, '200 Level'), (300, '300 Level'), (400, '400 Level')])),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='student_profiles/')),
                ('fingerprint1', models.TextField(blank=True, null=True)),
                ('fingerprint2', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
