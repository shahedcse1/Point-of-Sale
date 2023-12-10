from django.contrib import admin
from .models import Purchase

# Register your models here.
class PurchaseAdmin(admin.ModelAdmin):
    list_display = [
        'purchase_date', 
        'reference_no', 
        'supplier', 
        'purchase_type', 
        'discount', 
        'order_note',
        'shipping',
    ]
admin.site.register(Purchase, PurchaseAdmin)