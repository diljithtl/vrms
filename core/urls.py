from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('vehicles/', views.vehicle_management, name='vehicle_management'),
    path('drivers/', views.driver_management, name='driver_management'),

    path('customer/', views.customer_dashboard, name='customer_dashboard'),
    path('booking/', views.booking, name='booking'),
    path('payment/<int:id>/', views.payment, name='payment'),

    path('driver/', views.driver_dashboard, name='driver_dashboard'),

    path('error/', views.error, name='error'),
]
