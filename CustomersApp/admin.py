from django.contrib import admin
from .models import CustomerModel


# Register your models here.
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'slug', 
        'email', 
        'phone_number', 
        'country', 
        'address',
        'city',
        'state', 
        'coustomer_group', 
    ]
admin.site.register(CustomerModel, CustomerModelAdmin)
