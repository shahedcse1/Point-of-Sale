from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
class Category(models.Model):
    cate_image= models.ImageField(verbose_name='Category Image', upload_to='products/', blank=True)
    cate_name=models.CharField(verbose_name='Category name', max_length=100, unique=True)
    cate_shot_des = models.CharField(verbose_name='Category short description', max_length=200, blank=True)
    cate_des = models.TextField(verbose_name='Category description', blank=True)
    parent = models.ForeignKey('self', verbose_name='Parent Category',  on_delete=models.SET_NULL, blank=True, null=True, related_name='product_related')
    slug = models.SlugField(unique=True)
    code = models.CharField(verbose_name='Category code', max_length=50)
    is_active = models.BooleanField(verbose_name='Is Active', default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cate_name
        
    def image_url(self):
        try:
            url=self.cate_image.url
        except:
            url=''
        return url


    def save(self, *args, **kwargs):
        self.slug = slugify(self.cate_name)
        return super().save(*args, **kwargs)

    def get_update_url(self):
        return reverse("ProductApp:category-update", kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("ProductApp:category-detail", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("ProductApp:category-delete", kwargs={'slug':self.slug})
    


class Product(models.Model):
    Product_Type=(
        ('standart', 'standard'),
        ('conbo', 'combo'),
        ('digital', 'digital'),
    )
    product_type= models.CharField(choices=Product_Type, max_length=50, default='standard')
    tax=(
        ('Exclude', 'Exclude'),
        ('Include', 'Include'),
        ('None', 'None'),
        
    )
    name = models.CharField(max_length=60, unique=True)
    code = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    tax_mathod = models.CharField(choices=tax, max_length=50, default='None')
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    product_image= models.ImageField(verbose_name='Product Image', upload_to='products/', blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def image_url(self):
        try:
            url=self.product_image.url
        except:
            url=''
        return url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    
    def get_update_url(self):
        return reverse("ProductApp:product-update", kwargs={'slug':self.slug})

    def get_absolute_url(self):
        return reverse("ProductApp:product-detail", kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse("ProductApp:product-delete", kwargs={'slug':self.slug})




