from django.contrib import admin
from .models import CountryData, Product, Order
from django.contrib.auth.models import Group

admin.site.site_header = 'Ronald Inventory Dashboard'
# Register your models here.
admin.site.register(CountryData)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
