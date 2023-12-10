from django.urls import path
from django.conf.urls import include
from posadminApp.views import HomeView


app_name = 'posadminApp'
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]
