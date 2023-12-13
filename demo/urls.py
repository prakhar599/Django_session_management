from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('del/', views.delsession),
]