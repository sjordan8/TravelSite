from django.urls import include, path
import django.contrib.auth.urls
from . import views

urlpatterns = [
    path('', views.index),
    path('new_trip/', views.new_trip),
    path('trips/', views.trips),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register),
    path('logout_view/', views.logout_view),
]
