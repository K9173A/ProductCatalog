from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import Product
from .forms import ProductForm


def catalog(request):
    context = {
        'title': 'Каталог',
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/catalog.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:catalog'))
    else: # GET
        form = ProductForm()

    context = {
        'title': 'Новый продукт',
        'form': form
    }
    return render(request, 'mainapp/create_product.html', context)
