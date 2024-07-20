from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('apply_loan/', views.apply_loan, name='apply_loan'),
    path('register/', views.register, name='register'),  # Add the registration URL
    path('login/', views.login_view, name='login'),      # Add the login URL
    path('application/<int:application_id>/', views.view_application, name='view_application'), 
    path('logout/', logout_view, name='logout'),
    path('application/<int:pk>/', views.view_application, name='view_application'),
]
  

