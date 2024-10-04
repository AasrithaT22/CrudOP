from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10
    list_filter = ['name']
    search_fields = ['name']

@admin.register(models.Employee)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'role', 'domain', 'organization']
    list_editable = ['salary']
    list_per_page = 10
    search_fields = ['name']