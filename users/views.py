from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from locals.models import Local
from products.models import Product
from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import *


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['admin'])
def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, prefix='user')
        profile_form= ProfileForm(request.POST, prefix='userprofile')
        
        if user_form.is_valid and profile_form.is_valid:
            user = user_form.save()
            group = Group.objects.get(name='usuario')
            user.groups.add(group)
            user.save()
            userprofile = profile_form.save(commit=False)
            userprofile.user = user

            num = str(profile_form.cleaned_data.get('phone'))
            if len(num) == 10:
                phoneNum = ("("+num[:3]+")"+num[3:6]+"-"+num[6:])
            if len(num) == 7:
                phoneNum = ("(031)"+num[3:6]+"-"+num[6:])

            userprofile.phone = phoneNum
            userprofile.save()
            messages.success(request, f'La cuenta fue creada, ya puede Iniciar sesión!')
            return redirect('locals')
    else:
        user_form = UserRegisterForm(request.POST, prefix='user')
        profile_form= ProfileForm(request.POST, prefix='userprofile')
    
    context = {'title':'Registro', 'user_form':user_form, 'profile_form':profile_form}
    return render(request, 'users/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('locals')
        else:
            messages.info(request, 'Algo no salio bien, Intentalo de nuevo')

    title = 'Registro'
    context = {'title':title}
    return render(request, 'users/login.html', context)


def userLogout(request):
#     logout(request)
#     messages.success(request, f'Has terminado la sesión!')
#     return redirect('locauser = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, null=False, blank=False)
#     ccls')
    pass


@login_required
def userProfile(request):
    user = request.user
    user_locals = Local.objects.filter(person=user)
    objects = []
    counter = 0

    for local in user_locals:
        product = Product.objects.filter(local=local.id)
        for x in product:
            data = {'label': x.label, 'category':x.category, 'local':x.local, 'name':x.name, 'price':x.price, 'discount':x.discount, 'id':x.id}
            objects.append(data)
            counter = counter + 1

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

    context = {'title':'Perfil', 'user':user, 'user_locals':user_locals, 'objects':objects, 'counter':counter, 'page_range1':page_range1}
    return render(request, 'users/user_profile.html', context)


def editProfile(request):
    user = request.user.profile
    profile_form= ProfileForm(instance=user)

    if request.method == 'POST':
        profile_form= ProfileForm(request.POST, request.FILES, instance=user)
        
        if profile_form.is_valid:
            profile_form.save()
            messages.success(request, f'La cuenta fue modificada, ya puede Iniciar sesión!')
            return redirect('locals')
    else:
        profile_form= ProfileForm(instance=user)

    title = 'Modificar Perfil'
    context = {'title':title, 'profile_form':profile_form}
    return render(request, 'users/edit_profile.html', context)
