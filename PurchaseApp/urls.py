from django.urls import path
from django.conf.urls import include
from .views import PurchaseCreateView, PurchaseListView, PurchaseUpdateView, PurchaseDeleteView, PurchaseDetailView


app_name = 'PurchaseApp'
urlpatterns = [
    path('', PurchaseListView.as_view(), name='purchase-list'),
    path('add/', PurchaseCreateView.as_view(), name='purchase-add'),
    path('update/<slug:slug>/', PurchaseUpdateView.as_view(), name='purchase-update'),
    path('delete/<slug:slug>/', PurchaseDeleteView.as_view(), name='purchase-delete'),
    path('details/<slug:slug>/', PurchaseDetailView.as_view(), name='purchase-details'),

]


