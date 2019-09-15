from django.urls import path

from .views import catalog, create_product


app_name = 'mainapp'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('create_product/', create_product, name='create_product'),
]
