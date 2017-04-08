from __future__ import unicode_literals

from django.db import models

# Create your models here.
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    # PostModel = instance.__class__
    # new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(instance.name, filename)

class Product(models.Model):
    GAME_LEVEL = (('Hard', 'Hard'),('Normal', 'Normal'))
    name = models.CharField(max_length=100)
    photo = models.URLField(blank=True, default='', help_text='image link')
    level = models.CharField(max_length=20, choices=GAME_LEVEL, default='Normal')