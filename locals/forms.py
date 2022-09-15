from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *
from products.models import *


class CreateLocalForm(ModelForm):
    class Meta:
        model = Local
        fields = '__all__'

