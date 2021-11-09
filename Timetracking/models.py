from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class User_ext(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def total_hours(self):
        sum = 0.0
        for log in Log.objects.filter(user=self.user.id, paid=False):
            sum += (log.duration.total_seconds() / 3600.0)
        return sum


class Log(models.Model):
    class Meta:
        ordering = ['begin_dateTime']

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=2000)
    begin_dateTime = models.DateTimeField(default=timezone.now)
    end_dateTime = models.DateTimeField(default=timezone.now)
    pay_dateTime = models.DateTimeField(default=timezone.now)
    finished = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)

    @property
    def duration(self):
        return self.end_dateTime - self.begin_dateTime
