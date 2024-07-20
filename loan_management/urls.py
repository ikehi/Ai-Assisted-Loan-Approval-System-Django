from django.contrib import admin
from django.urls import path, include
from loans.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', include('loans.urls')),  # Include the registration path
    path('accounts/login/', include('loans.urls')),     # Include the login path
    path('loans/', include('loans.urls')),              # Include the URLs from the loans app
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
