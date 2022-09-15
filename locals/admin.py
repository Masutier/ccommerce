from django.contrib import admin
from .models import *


class LocalesAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor', 'localNum', 'active', 'activethru')


admin.site.register(Local, LocalesAdmin)
