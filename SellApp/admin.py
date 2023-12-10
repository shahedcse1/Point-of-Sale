from django.contrib import admin
from .models import SellModel

# Register your models here.
class SellModelAdmin(admin.ModelAdmin):
    list_display = [
        'sell_date', 
        'reference_no', 
        'biller', 
        'Customer', 
        'order_tax', 
        'order_discount',
        'shipping',
        'attach_doc', 
        'sale_status', 
        'payment_status',
        'sale_note',
    ]
admin.site.register(SellModel, SellModelAdmin)

