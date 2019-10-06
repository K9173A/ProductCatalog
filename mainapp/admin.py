"""
Module for admin part of the mainapp.
"""
from django.contrib import admin

from .models import Product


admin.site.register(Product)
