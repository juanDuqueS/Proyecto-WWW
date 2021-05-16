from django.urls import path
from buildingManagement import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('stock/', views.stock, name="Stock"),
    path('reports/', views.reports, name="Reports"),
    path('contact/', views.contact, name="Contact us"),
]