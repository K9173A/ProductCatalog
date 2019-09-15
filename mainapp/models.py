from django.db import models


class Product(models.Model):
    """Model which stores products."""
    name = models.CharField(
        verbose_name='Название',
        max_length=32
    )
    date = models.DateTimeField(
        verbose_name='Дата поступления',
        auto_now_add=True
    )
    measuring_system = models.CharField(
        verbose_name='Единцы измерения',
        max_length=32
    )
    provider = models.CharField(
        verbose_name='Поставщик',
        max_length=32
    )
