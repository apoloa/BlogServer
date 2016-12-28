from django.contrib import admin
from blogs.models import Category, Blog

# Register your models here.
admin.site.register(Category)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
