from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exploits/', views.exploits, name='exploits')
]