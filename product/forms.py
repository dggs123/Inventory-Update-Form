from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms import layout, bootstrap

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","photo","level"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']