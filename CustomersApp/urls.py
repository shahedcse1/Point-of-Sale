from django.urls import path
from .views import CustomerCreateView, CustomerListView, CustomerUpdateView, CustomerDeleteView, CustomerDetailView


app_name = 'CustomersApp'
urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('create/', CustomerCreateView.as_view(), name='customer-create'),
    path('update/<slug:slug>/', CustomerUpdateView.as_view(), name='customer-update'),
    path('delete/<slug:slug>/', CustomerDeleteView.as_view(), name='customer-delete'),
    path('details/<slug:slug>/', CustomerDetailView.as_view(), name='customer-details'),
]
