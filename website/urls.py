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
    path('', views.home, name='home'), #path to homepage if logged in, form for sign-in credentials
    path('logout/', views.logout_user, name='logout'), #path to logout function
    path('register/', views.register_user, name='register'), #path to registration or sign up form
    path('pets/', views.pets, name='pets'), #path to information of pets as objects
    path('customers/', views.customers, name='customers'), #path to information of customers as objects
    path('record/<int:pk>/', views.customer_record, name='record'), #path to view individual customer records
    path('delete_customer/<int:pk>/', views.delete_customer, name='delete_customer'), #path to deletion of indiv customer record
    path('add_customer/', views.add_customer, name='add_customer'), #path to adding customer forms
    path('update_customer/<int:pk>/', views.update_customer, name='update_customer'), #path to update customer forms
    path('update_pet/<int:pk>/', views.update_pet, name='update_pet'), #path to update pet information form
    path('pet_record/<int:pk>/', views.pet_record, name='pet_record'), #path to view individual pet records
    path('delete_pet/<int:pk>/', views.delete_pet, name='delete_pet'), #path to deleteion of indiv pet record
    path('add_pet/', views.add_pet, name='add_pet'), #path to adding pet records
]

print(views.__dict__)