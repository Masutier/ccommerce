from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=False, blank=False)
    cc = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
