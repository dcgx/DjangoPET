from django.contrib import admin
from .models import AnimalType, Pet


# Register your models here.

@admin.register(AnimalType, Pet)
class BaseAdminRegister(admin.ModelAdmin):
    pass
