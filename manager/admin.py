from django.contrib import admin
from .models import *


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('local', 'payday', 'monts', 'amount')


admin.site.register(Payment, PaymentAdmin)
