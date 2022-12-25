from django.shortcuts import render
from django.contrib import messages


def center(request):
    
    context = {'title': 'Centro Comercial'}
    return render(request, 'comercial/main.html', context)


def privacy(request):
    
    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'comercial/privacy.html', context)


def page401(request):

    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'comercial/status_codes/page401.html', context)

