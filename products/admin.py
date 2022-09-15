from django.contrib import admin
from .models import *


class ProductosAdmin(admin.ModelAdmin):
    list_display = ('label', 'category', 'name', 'local', 'price', 'discount')


admin.site.register(Product, ProductosAdmin)
