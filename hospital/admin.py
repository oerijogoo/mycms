from django.contrib import admin
from .models import Hospital


class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
# Register your models here.


admin.site.register(Hospital, HospitalAdmin)
