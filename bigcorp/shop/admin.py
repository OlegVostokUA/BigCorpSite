from django.contrib import admin
from .models import Category, Product, ProductManager, ProductProxy


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand', 'slug', 'price', 'available')
    list_editable = ('price', 'available')
    ordering = ('title',)
    list_filter = ('title', 'category', 'brand', 'price', 'available')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)