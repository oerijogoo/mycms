from django.contrib import admin
from .models import Roads
# Register your models here.


class RoadAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')


admin.site.register(Roads, RoadAdmin)
