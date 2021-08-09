from django.contrib import admin
from .views import Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'date_posted')


admin.site.register(Blog, BlogAdmin)
