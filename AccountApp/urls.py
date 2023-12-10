from django.urls import path
from django.conf.urls import include
from .views import AccountCreateView, AccountListView, AccountUpdateView

app_name = 'AccountApp'
urlpatterns = [
    path('', AccountListView.as_view(), name='account-list'),
    path('create/', AccountCreateView.as_view(), name='account-create'),
    path('update/<int:pk>/', AccountUpdateView.as_view(), name='account-update'),


]
