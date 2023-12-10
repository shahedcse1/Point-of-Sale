from django.urls import path
from django.conf.urls import include
from ProductApp.views import CategoryCreateView, CategoryList, CategoryUpdate, CategoryDetail, CategoryDelete, ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView, ProductDetailView


app_name = 'ProductApp'
urlpatterns = [
    #path('category/', CategoryCreateView.as_view(), name='category'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<slug:slug>/', CategoryUpdate.as_view(), name='category-update'),
    path('category/detail/<slug:slug>/', CategoryDetail.as_view(), name='category-detail'),
    path('category/delete/<slug:slug>/', CategoryDelete.as_view(), name='category-delete'),
    path('product/create/', ProductCreateView.as_view(), name='product-create'),
    path('product/list/', ProductListView.as_view(), name='product-list'),
    path('product/update/<slug:slug>/', ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<slug:slug>/', ProductDeleteView.as_view(), name='product-delete'),
    path('product/detail/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    
]
