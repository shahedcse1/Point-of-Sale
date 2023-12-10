from django.urls import path
from .views import SellCreateView, SellListView, SellUpdateView, SellDeleteView, SellDetailsView


app_name = 'SellApp'
urlpatterns = [
    path('', SellListView.as_view(), name='sale-list'),
    path('create/', SellCreateView.as_view(), name='sale-create'),
    path('update/<slug:slug>/', SellUpdateView.as_view(), name='sale-update'),
    path('delete/<slug:slug>/', SellDeleteView.as_view(), name='sale-delete'),
    path('details/<slug:slug>/', SellDetailsView.as_view(), name='sale-details'),
    

]


