from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'cate_name',
        'cate_shot_des',
        'cate_des',
        'cate_image',
        'parent',
        'slug',
        'code',
        'is_active'
    ]
    prepopulated_fields = {'slug': ('cate_name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'product_type',
        'name',
        'code',
        'product_category',
        'cost',
        'price',
        'tax_mathod',
        'quantity',
        'description',
        'product_image'
    ]
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product, ProductAdmin)


