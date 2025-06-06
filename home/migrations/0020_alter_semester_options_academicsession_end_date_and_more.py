# Generated by Django 5.1.6 on 2025-04-16 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_academicsession_is_current_semester_end_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['start_date']},
        ),
        migrations.AddField(
            model_name='academicsession',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='academicsession',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='max_level',
            field=models.IntegerField(choices=[(300, '300 Level (Regular)'), (400, '400 Level (Nursing)')], default=300),
        ),
        migrations.AddField(
            model_name='student',
            name='last_level_update',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Graduated', 'Graduated')], default='Active', max_length=20),
        ),
        migrations.AlterField(
            model_name='semester',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 12, 31)),
        ),
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(choices=[('First', 'First Semester (September-December)'), ('Second', 'Second Semester (January-April)'), ('Summer', 'Summer Semester (June-August)')], max_length=50),
        ),
        migrations.AlterField(
            model_name='semester',
            name='start_date',
            field=models.DateField(default=datetime.date(2024, 9, 1)),
        ),
    ]
