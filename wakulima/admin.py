from django.contrib import admin
from .models import Mkulima


class MkulimaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Mkulima, MkulimaAdmin)
