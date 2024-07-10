from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.order_home, name='order_home'),
    path('orders', views.create, name='create-order'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>', views.OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>', views.OrderDeleteView.as_view(), name='order-delete')

]