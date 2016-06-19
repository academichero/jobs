from django import forms
from .models import Job
from django.contrib.auth.models import User


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        exclude = ('author',)
