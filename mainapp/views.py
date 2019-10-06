"""
Module for mainapp views.
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Product
from .forms import ProductForm


def catalog(request):
    """
    Renders catalog and its items.
    :param request: request object.
    :return: rendered catalog page.
    """
    context = {
        'title': 'Каталог',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/catalog.html', context)


def create_product(request):
    """
    This view has 2 cases:
    1) POST-method: adds new item to the database and returns renewed list
       of products.
    2) GET-method: opens empty modal form.
    :param request: request object.
    :return: serialized form and list of products.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            products = Product.objects.all()
            data = {
                'form_is_valid': True,
                'products_html': render_to_string(
                    'mainapp/product_list.html',
                    context={'products': products},
                    request=request
                )
            }
        else:
            data = {
                'form_is_valid': False,
                'form_html': render_to_string(
                    'mainapp/create_product_form.html',
                    context={'form': form},
                    request=request
                )
            }
    else:
        data = {
            'form_html': render_to_string(
                'mainapp/create_product_form.html',
                context={'form': ProductForm()},
                request=request
            )
        }
    return JsonResponse(data)
