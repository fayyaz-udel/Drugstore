# Generated by Django 3.2.9 on 2021-11-06 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Timetracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(default=2000, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
