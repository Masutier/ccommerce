from django.db import models
from django.urls import reverse
from locals.models import Local

LABEL = (
    ('Usado', 'Usado'),
    ('Nuevo', 'Nuevo')
)
CATEGORY = (
    ('Computadores', 'Computadores'),
    ('Celulares', 'Celulares'),
    ('Accesorios', 'Accesorios'),
    ('Gamers', 'Gamers'),
    ('Impresoras', 'Impresoras'),
    ('Audiovisual', 'Audiovisual'),
    ('Servicios', 'Servicios'),
    ('Alimentos', 'Alimentos'),
)

class Product(models.Model):
    label = models.CharField(max_length=50, blank=True, null=True, default='Nuevo', choices=LABEL)
    category = models.CharField(max_length=50, blank=True, null=True, default='Computadores', choices=CATEGORY)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=60, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    discount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    foto1 = models.ImageField(default='img/products/default.png', upload_to='img/products')
    foto2 = models.ImageField(upload_to='img/products', blank=True, null=True)
    foto3 = models.ImageField(upload_to='img/products', blank=True, null=True)
    
    def __str__(self):
        return self.name

    def get_product_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
