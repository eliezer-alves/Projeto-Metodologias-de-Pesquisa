from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'city', 'user', 'bedrooms', 'toilets', 'peoples', 'price']