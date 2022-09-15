from django.shortcuts import render
from django.contrib import messages


def center(request):
    
    context = {'title': 'Centro Comercial'}
    return render(request, 'center/main.html', context)


def privacy(request):
    
    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'center/privacy.html', context)


def page401(request):

    context = {'title': 'Poliza de Privacidad'}
    return render(request, 'center/status_codes/page401.html', context)

