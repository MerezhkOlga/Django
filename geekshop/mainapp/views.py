from django.shortcuts import render

from .models import ProductCategory


def products(request):
    title = 'каталог'
    links_menu = ProductCategory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
    }
    return render(request, 'mainapp/products.html', context=context)