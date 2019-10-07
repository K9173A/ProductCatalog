"""
URL dispatcher of the mainapp.
"""
from django.urls import path

from .views import catalog, create_product, delete_product


app_name = 'mainapp'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('create_product/', create_product, name='create_product'),
    path('delete_product/<int:pk>/', delete_product, name='delete_product')
]
