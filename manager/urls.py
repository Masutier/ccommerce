from django.urls import path
from .views import *


urlpatterns = [
    path('manager', manager, name='manager'),
    path('managmentProducts', managmentProducts, name='managmentProducts'),
    path('managmentUsers', managmentUsers, name='managmentUsers'),

    path('managmentLocals', managmentLocals, name='managmentLocals'),
    path('editLocalAdmin/<int:pk>', editLocalAdmin, name='editLocalAdmin'),
    path('createLocal', createLocal, name='createLocal'),
    path('editLocal/<int:pk>', editLocal, name='editLocal'),
    path('deleteLocal/<int:pk>', deleteLocal, name='deleteLocal'),

    path('payment', payment, name='payment'),
    path('localPayments/<int:pk>', localPayments, name='localPayments'),
    path('createPayment', createPayment, name='createPayment'),
    path('editPayment/<int:pk>', editPayment, name='editPayment'),
    path('deletePayment/<int:pk>', deletePayment, name='deletePayment'),

]
