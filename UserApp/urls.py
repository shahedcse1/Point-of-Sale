from django.urls import path
from django.conf.urls import include
from .views import UserCreationView, UserListView, UserUpdateView

app_name = 'UserApp'
urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('create/', UserCreationView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),

]
