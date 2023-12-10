from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import CustomerModel
from .forms import CustomerForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.
class CustomerCreateView(CreateView):
    model = CustomerModel
    template_name = 'customersApp/customer_add.html'
    form_class = CustomerForm

    def get_success_url(self):
        messages.success(self.request, 'Your customer added ')
        return reverse('CustomersApp:customer-list')


class CustomerListView(ListView):
    model = CustomerModel
    template_name = 'customersApp/customer_list.html'
    context_object_name = 'customers'


class CustomerUpdateView(UpdateView):
    model = CustomerModel
    template_name = 'customersApp/customer_update.html'
    form_class = CustomerForm

    def get_success_url(self):
        messages.success(self.request, 'Your customer updated')
        return reverse('CustomersApp:customer-list')


class CustomerDeleteView(DeleteView):
    model = CustomerModel
    template_name = 'customersApp/customer_delete.html'
    context_object_name = 'customer'

    def get_success_url(self):
        messages.success(self.request, 'Your customer delete')
        return reverse('CustomersApp:customer-list')


class CustomerDetailView(DetailView):
    model = CustomerModel
    template_name = 'customersApp/customer_details.html'
    context_object_name = 'customer_details'


