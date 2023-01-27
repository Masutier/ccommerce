from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from locals.forms import *
from locals.models import *
from products.models import *
from users.decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import *
from .utils import concat_ints


@admin_only
def manager(request):
    locales_active = Local.objects.filter(active=True)
    locales_not_active = Local.objects.filter(active=False)
    all_locals = Local.objects.all().order_by('id')
    totalLocales = all_locals.count()

    productos = Product.objects.all()
    products_count = productos.count()

    usuarios = User.objects.all()
    users_count = usuarios.count()

    context = {'title':'Administración', 'totalLocales':totalLocales, 'all_locals':all_locals, 'locales_active':locales_active,
     'locales_not_active':locales_not_active, 'products_count':products_count, 'users_count':users_count}
    return render(request, 'manager/manager.html', context)


# LOCALS
@admin_only
def managmentLocals(request):
    objects = Local.objects.all().order_by('id')
    totalLocales = objects.count()
    
    # pagination
    paginator = Paginator(objects, 13)
    page = request.GET.get('page1')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    index1 = objects.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    context = {'title':'Admin Locals', 'objects':objects, 'totalLocales':totalLocales, 'page_range1':page_range1}
    return render(request, 'manager/manager_locals.html', context)


@admin_only
def createLocal(request):
    locales_all = Local.objects.all().order_by('floor', 'localNum')
    all_locals = locales_all

    if request.method == 'POST':
        form = CreateLocalForm(request.POST, request.FILES)
        if form.is_valid():
            dataForm = form.save(commit=False)
            localNum = form.cleaned_data.get('localNum')
            floor = form.cleaned_data.get('floor')
            dataForm.id = concat_ints(floor, localNum)
            for local in locales_all:
                if local.floor ==  dataForm.floor:
                    if local.localNum ==  dataForm.localNum:
                        messages.error(request, f'El Numero de local ya existe!')
                        return redirect('managmentLocals')

            num = str(form.cleaned_data.get('phone'))
            if len(num) == 10:
                phoneNum = ("("+num[:3]+")"+num[3:6]+"-"+num[6:])
            if len(num) == 7:
                phoneNum = ("(031)"+num[3:6]+"-"+num[6:])

            dataForm.phone = phoneNum
            dataForm.save()
            messages.success(request, f'El local ya quedo guardado!')
            return redirect('managmentLocals')

    else:
        form = CreateLocalForm()

    title = 'Crear Local'
    context = {'title':title, 'form':form, 'locales':locales_all, 'all_locals':all_locals}
    return render(request, 'manager/logs/create_local.html', context)


@admin_only
def editLocal(request, pk):
    local = Local.objects.get(id=pk)
    form = CreateLocalForm(instance=local)
    if request.method == 'POST':
        form = CreateLocalForm(request.POST, request.FILES, instance=local)
        if form.is_valid():
            form.save()
            messages.success(request, f'El local ya quedo Modificado!')
            return redirect('detailLocal', local.pk)

    title = 'Editar Local'
    context = {"title": title, "form": form, 'local':local}
    return render(request, 'manager/logs/edit_local.html', context)


@admin_only
def deleteLocal(request, pk):
    local = Local.objects.get(id=pk)
    if request.method == 'POST':
        local.delete()
        messages.success(request, f'El local ya quedo eliminado!')
        return redirect ('managmentLocals')

    title = 'Eliminar Local'
    context = {'title':title, 'local':local}
    return render(request, 'manager/logs/delete_local.html', context)


@admin_only
def editLocalAdmin(request, pk):
    local = Local.objects.get(id=pk)
    form = CreateLocalForm(instance=local)
    if request.method == 'POST':
        form = CreateLocalForm(request.POST, request.FILES, instance=local)
        if form.is_valid():
            form.save()
            messages.success(request, f'El local ya quedo Modificado!')
            return redirect('managmentLocals')

    context = {'title':'Editar Local', 'form':form}
    return render(request, 'manager/logs/edit_local_admin.html', context)


# PRODUCTS
@admin_only
def managmentProducts(request):
    objects = Product.objects.all()
    products_count = objects.count()
    all_locals = Local.objects.all().order_by('id')

    # pagination == objects
    paginator = Paginator(objects, 13)
    page = request.GET.get('page1')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    index1 = objects.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    context = {'title':'Administración', 'objects':objects, 'products_count':products_count, 'page_range1':page_range1, 'all_locals':all_locals}
    return render(request, 'manager/manager_products.html', context)


# USERS
@admin_only
def managmentUsers(request):
    objects = User.objects.all()
    users_count = objects.count()
    all_locals = Local.objects.all().order_by('id')

    # pagination == objects
    paginator = Paginator(objects, 13)
    page = request.GET.get('page1')
    try:
        objects = paginator.page(page)
    except PageNotAnInteger:
        objects = paginator.page(1)
    except EmptyPage:
        objects = paginator.page(paginator.num_pages)
    index1 = objects.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    context = {'title':'Administración', 'objects':objects, 'users_count':users_count, 'page_range1':page_range1, 'all_locals':all_locals}
    return render(request, 'manager/manager_users.html', context)


# PAYMENTS
@admin_only
def payment(request):
    obj = Payment.objects.all().order_by('local')
    
    context = {'title':'Pagos', 'obj':obj}
    return render(request, 'manager/payments/payments.html', context)


@admin_only
def localPayments(request, pk):
    localPay = Payment.objects.filter(local=pk)

    context = {'title':'Pagos', 'localPay':localPay}
    return render(request, 'manager/payments/local_payment.html', context)


@admin_only
def createPayment(request):
    today = datetime.date(datetime.now())

    if request.method == 'POST':
        form = CreatePaymentForm(request.POST)
        if form.is_valid:
            payForm = form.save(commit=False)
            locId = str(form.cleaned_data.get('local'))
            payDay = form.cleaned_data.get('payday')
            montsPay = form.cleaned_data.get('monts')
            
            localPay = Local.objects.get(id=locId)
            localPay.lastPay = payDay
            localPay.activethru = localPay.activethru + relativedelta(months=montsPay)

            if localPay.activethru < today:
                localPay.active = False
            else:
                localPay.active = True

            payForm.save()
            localPay.save()
            messages.success(request, f'El Pago ya quedo agregado!')
            return redirect('payment')
    else:
        form = CreatePaymentForm()

    context = {'title':'Pagos', 'form':form}
    return render(request, 'manager/payments/create_payment.html', context)


@admin_only
def editPayment(request, pk):
    pay = Payment.objects.get(id=pk)
    form = CreatePaymentForm(instance=pay)
    if request.method == 'POST':
        form = CreatePaymentForm(request.POST, instance=pay)
        if form.is_valid():
            form.save()
            return redirect('payment')
    
    context = {'title':'Editar Pagos', 'form':form}
    return render(request, 'manager/payments/edit_payment.html', context)


@admin_only
def deletePayment(request, pk):
    pay = Payment.objects.get(id=pk)

    if request.method == 'POST':
        pay.delete()
        messages.success(request, f'El pago ya quedo eliminado!')
        return redirect ('editLocalAdmin', pay.local)

    context = {'title':'Eliminar Pagos', 'pay':pay}
    return render(request, 'manager/payments/delete_payment.html', context)
