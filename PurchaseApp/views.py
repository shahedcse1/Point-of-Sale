from django.db import models
from django.shortcuts import render
from .models import Purchase
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.contrib import messages
from django.urls import reverse
from .forms import PurchaseFrom
from ProductApp.models import Product


#Create your views here.
class PurchaseCreateView(CreateView):
    model = Purchase
    template_name = "purchaseApp/purchase_add.html"
    form_class = PurchaseFrom

    def get_success_url(self):
        messages.success(self.request, 'Your purchase added ')
        return reverse('PurchaseApp:purchase-list')


class PurchaseListView(ListView):
    model = Purchase
    template_name = "purchaseApp/purchase_list.html"
    context_object_name = 'all_purchase'


class PurchaseUpdateView(UpdateView):
    model = Purchase
    fields = ('purchase_date',
        'reference_no',
        'supplier',
        'purchase_type',
        'discount',
        'order_note',
        'shipping')
    template_name= 'purchaseApp/purchase_update.html'
    def get_success_url(self):
        messages.success(self.request, 'Your purchase updated')
        return reverse('PurchaseApp:purchase-list')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    fields = ('purchase_date',
        'reference_no',
        'supplier',
        'purchase_type',
        'discount',
        'order_note',
        'shipping')
    template_name= 'purchaseApp/purchase_delete.html'
    context_object_name = 'purchase'
    def get_success_url(self):
        messages.success(self.request, 'Your purchase delated')
        return reverse('PurchaseApp:purchase-list')


class PurchaseDetailView(DetailView):
    model = Purchase
    fields = ('purchase_date',
        'reference_no',
        'supplier',
        'purchase_type',
        'discount',
        'order_note',
        'shipping')
    template_name= 'purchaseApp/purchase_detail.html'
    context_object_name = 'purchase_details'