from django.contrib import admin
from .models import AccountModel

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'phone_number',
        'email',
        'gender',
        'user'
    ]
admin.site.register(AccountModel, AccountAdmin)
