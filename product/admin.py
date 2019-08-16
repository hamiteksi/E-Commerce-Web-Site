from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'status',
        'category',
        'price',
        'stock',
    )
    list_filter = ('status', 'category', )
    list_editable = (
        'title',
        'status',
        'category',
        'price',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'status',
        'gender',
    )
    list_filter = ('status', )
    list_editable = (
        'title',
        'gender',
        'status',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
