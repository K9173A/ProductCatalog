"""
Module for mainapp forms.
"""
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """ProductForm allows to create new products."""
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Restyles form widgets with Twitter Bootstrap classes.
        :param args: additional parameters.
        :param kwargs: additional key-value parameters.
        """
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
