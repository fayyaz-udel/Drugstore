# Generated by Django 3.2.9 on 2021-11-08 14:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Timetracking', '0005_auto_20211106_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='pay_dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
