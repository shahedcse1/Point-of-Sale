import django
from django.db import models
from django.forms import forms
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import SellModel
from .forms import SellForm
from django.contrib import messages
from django.urls import reverse

# Create your views here.

class SellCreateView(CreateView):
    model = SellModel
    template_name = 'sellApp/sell_create.html'
    form_class = SellForm

    def get_success_url(self):
        messages.success(self.request, 'Sell created successfull')
        return reverse('SellApp:sale-list')



class SellListView(ListView):
    model = SellModel
    context_object_name = 'all_sell'
    template_name = 'sellApp/sell_list.html'
    form_class = SellForm


class SellUpdateView(UpdateView):
    model = SellModel
    template_name = 'sellApp/sell_update.html'
    form_class = SellForm
    def get_success_url(self):
        messages.success(self.request, 'Sell updated successfull')
        return reverse('SellApp:sale-list')


class SellDeleteView(DeleteView):
    model = SellModel
    template_name = 'sellApp/sell_delete.html'
    context_object_name = 'sales'

    def get_success_url(self):
        messages.success(self.request, 'Sell delete successfull')
        return reverse('SellApp:sale-list')


class SellDetailsView(DetailView):
    model = SellModel
    template_name = 'sellApp/sell_details.html'
    context_object_name = 'sale_details'
