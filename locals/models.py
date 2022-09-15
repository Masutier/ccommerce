from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Local(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    floor = models.DecimalField(max_digits=2, decimal_places=0, null=False, blank=False)
    localNum = models.DecimalField(max_digits=4, decimal_places=0, null=False, blank=False)
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    webpage = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=False, blank=False)
    logo = models.ImageField(default='img/logos/default.png', upload_to='img/logos/')
    localFoto = models.ImageField(default='img/locals/logolocal.png', upload_to='img/locals/')
    active = models.BooleanField(default=False, blank=False, null=True)
    outstand = models.BooleanField(default=True, blank=True)
    lastPay = models.DateField(auto_now_add=False, auto_now=False)
    activethru = models.DateField(auto_now_add=False, auto_now = False, blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detailLocal", kwargs={"pk": self.pk})
