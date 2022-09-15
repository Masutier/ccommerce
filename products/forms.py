from django.db import models
from django.forms import ModelForm
from django import forms
from locals.models import *
from products.models import *


class CreateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

