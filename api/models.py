from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class Light(models.Model):
    color = ColorField(default='#FFFFFF')
    state = models.BooleanField(default = False)
