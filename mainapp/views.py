from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Product
from .forms import ProductForm


def catalog(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/catalog.html', context)


def save_good_product(request, form, template):
    data = {}
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data = {
                'form_is_valid': True,
                'html_product_list': render_to_string(
                    'mainapp/product_list.html',
                    context={'products': Product.objects.all()},
                    request=request
                )
            }
        else:
            data['form_is_valid'] = False

    data['html_form'] = render_to_string(
        template,
        context={'form': form},
        request=request
    )
    return JsonResponse(data)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        return save_good_product(request, form, 'mainapp/create_product.html')
    else:
        return JsonResponse({
            'html_form': render_to_string(
                'mainapp/create_product.html',
                context={
                    'form': ProductForm(),
                    'title': 'Новый продукт'
                },
                request=request
            )
        })
