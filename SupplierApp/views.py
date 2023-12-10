from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Supplier
from django.contrib import messages
from django.urls import reverse
from .forms import SupplierForm

# Create your views here.
class SupplierCreateView(CreateView):
    model = Supplier
    fields = ('supplier_name', 'phone_number', 'address', 'city', 'country')
    template_name = "supplierApp/supplier_add.html"
    form_classes = SupplierForm

    def get_success_url(self):
        messages.success(self.request, 'Your supplier added ')
        return reverse('SupplierApp:supplier-list')


class SupplierListView(ListView):
    model = Supplier
    fields = ('supplier_name', 'phone_number', 'address', 'city', 'country')
    template_name = "supplierApp/supplier_list.html"
    context_object_name='suppliers'


class SupplierUpdateView(UpdateView):
    model = Supplier
    # fields = ('supplier_name', 'phone_number', 'address', 'city', 'country')
    template_name = "supplierApp/supplier_update.html"
    form_class = SupplierForm
    context_object_name='supplier'


    def get_success_url(self):
        messages.success(self.request, 'Your supplier updated ')
        return reverse('SupplierApp:supplier-list')


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "supplierApp/supplier_delete.html"
    context_object_name='supplier'

    def get_success_url(self):
        messages.success(self.request, 'Your supplier deleted ')
        return reverse('SupplierApp:supplier-list')


class SupplierDetailView(DetailView):
    model = Supplier
    fields = ('supplier_name', 'phone_number', 'address', 'city', 'country')
    template_name = "supplierApp/supplier_details.html"
    context_object_name='suppliers'
