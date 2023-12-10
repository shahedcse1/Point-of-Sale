from django.contrib import admin
from .models import Supplier


# Register your models here.
class SupplierAdmin(admin.ModelAdmin):
    list_display = [
        'supplier_name',
        'phone_number',
        'address',
        'city',
        'country'
    
    ]
admin.site.register(Supplier, SupplierAdmin)
