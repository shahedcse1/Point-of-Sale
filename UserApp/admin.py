from django.contrib import admin
from .models import UserModel

# Register your models here.
class UserCreationAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'phone_number',
        'email',
        'gender',
        'user'
    ]
admin.site.register(UserModel, UserCreationAdmin)

