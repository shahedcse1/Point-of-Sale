from django.db import models
from django.db.models.fields import DateField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse



# Create your models here.
class Biller(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)


class SellModel(models.Model):
    slug = models.SlugField(unique=True)
    sell_date = models.DateField()
    reference_no = models.CharField(max_length=50, unique=True)
    biller = models.ForeignKey(Biller, on_delete=models.SET_NULL, blank=True, null=True, related_name='biller')
    Customer = models.CharField(max_length=200)
    ORDER_TAX={
        ('No tax','No tax'),
        ('GST @5%', 'GST @5%'),
        ('VAT @10%', 'VAT @10%'),
    }
    order_tax = models.CharField(choices=ORDER_TAX, max_length=50)
    order_discount = models.IntegerField(default=0, validators= [MinValueValidator(0), MaxValueValidator(100)])
    shipping = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    attach_doc = models.FileField(upload_to='files/', blank=True)
    SALE_STATUS={
        ('Completed', 'Completed'),
        ('Pending', 'Pending')
    }
    sale_status = models.CharField(choices=SALE_STATUS, max_length=50)
    PAYMENT_STATUS={
        ('Pending', 'Pending'),
        ('Dew', 'Dew'),
        ('Payment', 'Payment'),
    }

    payment_status = models.CharField(choices=PAYMENT_STATUS, max_length=50)
    sale_note= models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.reference_no


    def save(self, *args, **kwargs):
        self.slug=slugify(self.reference_no)
        return super().save(*args, **kwargs)


    
    def get_update_url(self):
        return reverse('SellApp:sale-update', kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("SellApp:sale-details", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("SellApp:sale-delete", kwargs={'slug':self.slug})


