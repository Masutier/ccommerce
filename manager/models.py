from django.db import models
from django.urls import reverse
from locals.models import Local


class Payment(models.Model):
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    payday = models.DateField(auto_now_add=False, auto_now=False)
    monts = models.DecimalField(max_digits=2, default=1, decimal_places=0, null=False, blank=False)
    amount = models.CharField(max_length=10, default='20000', blank=False, null=False)

    def __str__(self):
        return str(self.local)
   
