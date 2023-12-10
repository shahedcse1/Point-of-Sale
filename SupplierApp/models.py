from django.db import models
from django.urls import reverse

# Create your models here.
class Supplier(models.Model):
    supplier_name=models.CharField(verbose_name='Supplier name', max_length=100, unique=True)
    phone_number = models.CharField(verbose_name='phone Number', max_length=50)
    address = models.TextField(verbose_name='Address', blank=True)
    city= models.CharField(verbose_name='City', max_length=100)
    country= models.CharField(verbose_name='Country', max_length=100) 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.supplier_name


    def get_update_url(self):
        return reverse("SupplierApp:supplier-update", kwargs={'pk':self.pk})

    def get_absolute_url(self):
        return reverse("SupplierApp:supplier-details", kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse("SupplierApp:supplier-delete", kwargs={'pk':self.pk})