from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import Product


class ProductForm(ModelForm):

    def clean_name(self):
        name = str(self.cleaned_data['name'])

        if len(Product.objects.filter(name=name))>0:
            raise forms.ValidationError('Product Already Exist')

        return name

    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'product_type', 'cover']
        labels = {
            'price': _('Price'),
            'cover': _('Cover Image'),

        }