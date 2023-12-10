from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AccountModel(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    GENDER = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    gender = models.CharField(choices=GENDER, max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='related_user')

    
    def __str__(self):
        return self.name

    