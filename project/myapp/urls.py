from django.urls import include, path
import django.contrib.auth.urls
from . import views

urlpatterns = [
    path('', views.index),
    path('profile/', views.profile),
    path('new_trip/', views.new_trip),
    path('trips/', views.trips),
    path('login/', views.login_view),
    path('register/', views.register),
    path('logout_view/', views.logout_view),
]
