from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from products.models import Product


def locals(request):
    locales_all = Local.objects.filter(active=True).order_by('id')

    context = {'title':'Locales', 'locales':locales_all}
    return render(request, 'locals/salon.html', context)


def detailLocal(request, pk):
    local = get_object_or_404(Local, id=pk)
    objects = Product.objects.filter(local=local.id)
    totalProducts = Product.objects.filter(local=local.id).count()

    if local.active == True:
        objects = Product.objects.filter(local=local.id).order_by('id')

    loc_num = str(local.floor) + "-" + str(local.localNum)
    title = 'Local ' + loc_num

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

    if request.user.is_authenticated:
        userActive = request.user
        if userActive == local.person:
            user_prof = request.user.profile
            context = {'title':title,  'local':local, 'objects':objects, 'userActive':userActive, 'user_prof':user_prof, 'page_range1':page_range1, 'totalProducts': totalProducts}
        else:
            context = {'title':title,  'local':local, 'objects':objects, 'page_range1':page_range1, 'totalProducts': totalProducts}
    else:
        context = {'title':title,  'local':local, 'objects':objects, 'page_range1':page_range1, 'totalProducts': totalProducts}
    
    return render(request, 'locals/local.html', context)
