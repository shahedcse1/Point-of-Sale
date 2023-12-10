from django.db import models
from django.db.models.fields import SlugField
from django.urls.base import reverse
from django.utils.text import slugify


# Create your models here.
class CustomerModel(models.Model):
    name = models.CharField(max_length=150)
    slug = SlugField(unique=True)
    email = models.EmailField(max_length=100)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    coustomer_group = models.CharField(max_length=100)
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def save(self, *agrs, **kwargs):
        self.slug=slugify(self.name)
        return super().save(*agrs, **kwargs)

    def get_update_url(self):
        return reverse("CustomersApp:customer-update", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('CustomersApp:customer-delete', kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("CustomersApp:customer-details", kwargs={"slug": self.slug})
    



