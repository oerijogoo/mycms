from django.contrib import admin
from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'county')


admin.site.register(Customer, CustomerAdmin)