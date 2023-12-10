from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Category, Product
from .forms import CategoryForm, ProductForm
from django.urls import reverse
from django.contrib import messages

# Create your views here.

#category
class CategoryCreateView(CreateView):
    model = Category
    fields = ('cate_name', 'parent', 'cate_image', 'code', 'is_active')
    template_name = "productApp/prod_add_category.html"
    form_classes = CategoryForm

    def get_success_url(self):
        messages.success(self.request, 'Your category added ')
        return reverse('posadminApp:home')


class CategoryList(ListView):
    model=Category
    context_object_name = 'Categories'
    template_name= 'productApp/product_category_list.html'


class CategoryUpdate(UpdateView):

    model = Category
    fields = ('cate_name', 'parent', 'cate_image', 'code', 'is_active')
    template_name= 'productApp/product_category_update.html'
    def get_success_url(self):
        messages.success(self.request, 'Your category updated ')
        return reverse('ProductApp:category-list')


class CategoryDelete(DeleteView):
    model = Category
    template_name= 'productApp/product_category_delete.html'
    context_object_name = 'category'
    def get_success_url(self):
        messages.success(self.request, 'Your category Deleted ')
        return reverse('ProductApp:category-list')


class CategoryDetail(DetailView):
    model = Category
    template_name= 'productApp/product_category_detail.html'
    context_object_name = 'category_details'


#product
class ProductCreateView(CreateView):
    model = Product
    fields = ('product_type', 'name', 'code', 'price', 'product_category', 'cost', 'tax_mathod', 'quantity', 'description', 'product_image')

    template_name = "productApp/product_add.html"
    form_classes = ProductForm

    def get_success_url(self):
        messages.success(self.request, 'Your product{0} added'.format(self.object))
        return reverse('ProductApp:product-list')


class ProductListView(ListView):
    model = Product
    fields = ('product_type', 'name', 'code', 'price', 'product_category', 'cost', 'tax_mathod', 'quantity', 'description', 'product_image')
    context_object_name = 'products'
    template_name = "productApp/product_list.html"



class ProductUpdateView(UpdateView):
    model = Product
    fields = ('product_type', 'name', 'code', 'price', 'product_category', 'cost', 'tax_mathod', 'quantity', 'description', 'product_image')

    template_name = "productApp/product_update.html"
    form_classes = ProductForm

    def get_success_url(self):
        messages.success(self.request, 'Your product updated ')
        return reverse('ProductApp:product-list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name= 'productApp/product_delete.html'
    context_object_name = 'product'
    def get_success_url(self):
        messages.success(self.request, 'Your product Deleted ')
        return reverse('ProductApp:product-list')


class ProductDetailView(DetailView):
    model = Product
    template_name= 'productApp/product_detail.html'
    context_object_name = 'product_details'



