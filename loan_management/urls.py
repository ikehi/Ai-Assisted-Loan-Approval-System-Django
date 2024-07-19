from django.contrib import admin
from django.urls import path, include
from loans.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', include('loans.urls')),  # Include the registration path
    path('accounts/login/', include('loans.urls')),     # Include the login path
    path('loans/', include('loans.urls')),              # Include the URLs from the loans app
]
