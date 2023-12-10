from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField
from django.urls.base import reverse
from django.utils.text import slugify
from SupplierApp.models import Supplier
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Purchase(models.Model):
    RECEIVE_TYPE=(
        ('Received', 'Received'),
        ('Not Received', 'Not Received')
    )
    slug = models.SlugField(unique=True)
    purchase_date= models.DateField()
    reference_no=models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, max_length=150, on_delete=models.CASCADE, related_name='purchase_suplliar')
    purchase_type = models.CharField(choices=RECEIVE_TYPE, max_length=50, default='Received')
    discount = models.IntegerField(default=0, validators= [MinValueValidator(0), MaxValueValidator(100)])
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    order_note = models.TextField(blank=True)
    shipping = models.DecimalField(max_digits=9, decimal_places=2, blank=True)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.reference_no)
        return super().save(*args, **kwargs)


    def get_update_url(self):
        return reverse('PurchaseApp:purchase-update', kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("PurchaseApp:purchase-details", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("PurchaseApp:purchase-delete", kwargs={'slug':self.slug})


