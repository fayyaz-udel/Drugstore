from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Log


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ["begin_dateTime", "end_dateTime", "user"]
        widgets = {
            'begin_dateTime': DateTimeInput(),
            'end_dateTime': DateTimeInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LogForm, self).__init__(*args, **kwargs)
        log = Log.objects.filter(user=self.user).first()

    def clean(self):
        cleaned_data = super().clean()
        begin_dateTime = cleaned_data.get("begin_dateTime")
        end_dateTime = cleaned_data.get("end_dateTime")

        if end_dateTime and begin_dateTime:
            if end_dateTime < begin_dateTime:
                raise ValidationError("End time cannot be sooner than begin time")


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "last_name", "first_name")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
