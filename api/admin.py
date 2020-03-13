from django.contrib import admin
from .models import Light
# Register your models here.
@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    list_display = ("color", "state")