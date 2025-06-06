# Generated by Django 5.1.6 on 2025-03-06 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fingerprint', '0002_student_delete_fingerprint'),
        ('home', '0009_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='FingerprintData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fingerprint_data', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
