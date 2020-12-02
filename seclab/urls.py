"""
 URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Home page
    path('', include('app.urls')),
    # Exploits page
    path('exploits/', include('app.urls')),
    # Admin page
    path('admin/', admin.site.urls),
]
