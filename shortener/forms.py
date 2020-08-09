from django.forms import ModelForm
from .models import *


class DashboardForm(ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'phone', 'profile_pic']
