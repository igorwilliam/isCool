from django.contrib import admin

from .models import Material

class MaterialAdmin(admin.ModelAdmin):
    list_filter = ['material']

admin.site.register(Material)
