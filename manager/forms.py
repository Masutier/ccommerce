from django.db import models
from django.forms import ModelForm
from django import forms
from .models import *


class CreatePaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
