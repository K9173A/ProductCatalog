"""
Module for mainapp models.
"""
from django.db import models


class Product(models.Model):
    """Model which stores products."""
    UNITS = (
        (0, 'шт.'),
        (1, 'кг.'),
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = models.CharField(
        verbose_name='Name',
        max_length=128
    )
    date = models.DateField(
        verbose_name='Date'
    )
    price = models.PositiveIntegerField(
        verbose_name='Price',
        default=0
    )
    unit = models.IntegerField(
        verbose_name='Unit',
        choices=UNITS,
        default=0
    )
    provider = models.CharField(
        verbose_name='Provider',
        max_length=128,
        blank=True
    )
