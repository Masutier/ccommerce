from django.urls import path, include
from .views import *


urlpatterns = [
    path('Salon', locals, name='locals'),
    path('Local/<int:pk>', detailLocal, name='detailLocal'),

]
