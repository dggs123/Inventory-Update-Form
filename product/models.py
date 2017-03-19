from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    PRODUCT_TYPE = (
        ('tv', 'TV'),
        ('refrigerator', 'Refrigerator'),
        ('ac', 'AC'),
        ('washing_machine', 'Washing Machine'),
    )

    name = models.CharField(max_length=100)
    price = models.IntegerField(help_text='Numeric, Eg: 50000')
    quantity = models.IntegerField(help_text='Numeric, Eg: 35')
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE, default='tv', blank=True, null=True)
    cover = models.URLField(blank=True, default='', help_text='image link for cover')