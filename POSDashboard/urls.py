from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posadminApp.urls')),
    path('product/', include('ProductApp.urls', namespace='ProductApp')),
    path('supplier/', include('SupplierApp.urls', namespace='SupplierApp')),
    path('purchase/', include('PurchaseApp.urls', namespace='PurchaseApp')),
    path('sell/', include('SellApp.urls', namespace='SellApp')),
    path('customers/', include('CustomersApp.urls', namespace='CustomersApp')),
    path('user/', include('UserApp.urls', namespace='UserApp')),
    path('account/', include('AccountApp.urls', namespace='AccountApp')),
    path('__debug__/', include('debug_toolbar.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    