from django.urls import path

from . import views

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Exploits page
    path('exploits/', views.exploits, name='exploits')
]
