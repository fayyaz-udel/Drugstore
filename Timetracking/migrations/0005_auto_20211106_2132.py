# Generated by Django 3.2.9 on 2021-11-07 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Timetracking', '0004_auto_20211106_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='log',
            name='paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='log',
            name='begin_dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='log',
            name='end_dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
