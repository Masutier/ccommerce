from django.urls import path, include
from .views import *


urlpatterns = [
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('promotions', promotions, name='promotions'),
    
    path('createProductByAdmin', createProductByAdmin, name='createProductByAdmin'),
    path('createProductByUser', createProductByUser, name='createProductByUser'),
    path('edit_product/<int:pk>', edit_product, name='edit_product'),
    path('delete_product/<int:pk>', delete_product, name='delete_product'),
    
]
