from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import *
from .models import *
from locals.models import Local
from users.decorators import allowed_users, admin_only
from manager.utils import concat_ints


def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)

    context = {'title':'Detalle', 'product':product}
    return render(request, 'products/product_detail.html', context)


def promotions(request):
    objects = Product.objects.all().exclude(discount__isnull=True)
    totalProducts = Product.objects.all().exclude(discount__isnull=True).count()

    # pagination
    paginator = Paginator(objects, 12)
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

    context = {'title':'Promociones', 'objects':objects, 'totalProducts':totalProducts, 'page_range1':page_range1}
    return render(request, 'products/promotions.html', context)


@login_required(login_url='loginPage')
@admin_only
def createProductByAdmin(request):
    locals = Local.objects.all()
    
    if request.method == 'POST':
        form = CreateProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            messages.success(request, f'El producto ya quedo guardado!')
            return redirect('managmentLocals')
    else:
        form = CreateProductForm()
    
    context = {'title':'Crear Producto', 'form':form, 'locals':locals}
    return render(request, 'products/logs/create_product_by_admin.html', context)
    

@login_required(login_url='loginPage')
def createProductByUser(request):
    user = request.user.id
    user_locals = Local.objects.filter(person=user)
    prodForm = CreateProductForm(request.POST, request.FILES)

    if prodForm.is_valid():
        localNum = prodForm.cleaned_data.get("local")
        for local in user_locals:
            if str(localNum) == str(local.id):
                prodForm.save()
                messages.success(request, f'El producto ya quedo guardado!')
                return redirect('userProfile')
        messages.success(request, f'El Local no pertenece a usted intente de nuevo!')
    else:
        prodForm = CreateProductForm()
    
    context = {'title':'Crear Producto by User', 'prodForm':prodForm, 'user_locals':user_locals}
    return render(request, 'products/logs/create_product_by_user.html', context)


@login_required(login_url='loginPage')
def edit_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    prodForm = CreateProductForm(instance=product)

    if request.method == 'POST':
        prodForm = CreateProductForm(request.POST, request.FILES, instance=product)
        if prodForm.is_valid():
            prodForm.save()
            messages.success(request, f'El producto ya quedo modificado!')
            return redirect('userProfile')

    context = {'title':'Editar Producto', 'prodForm':prodForm}
    return render(request, 'products/logs/edit_product.html', context)


@login_required(login_url='login')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('userProfile')

    context = {'title':'Eliminar Producto', 'item': product}
    return render(request, 'products/logs/delete_product.html', context)

