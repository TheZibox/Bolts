from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home_view'),
    path('generic/', views.GenericView.as_view(), name = 'generic_view'),
    path('elements/', views.ElementsView.as_view(), name = 'elements_view'),
]
