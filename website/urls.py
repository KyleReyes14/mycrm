"""
URL configuration for ncrm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('pets/', views.pets, name='pets'),
    path('customers/', views.customers, name='customers'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'),
    path('pet_record/<int:pk>/', views.pet_record, name='pet_record'),
    path('delete_pet/<int:pk>/', views.delete_pet, name='delete_pet'),
]

print(views.__dict__)