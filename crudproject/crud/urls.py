from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('new-employee', views.newEmployee),
    path('add-employee', views.addEmployee),
    path('employees', views.viewEmployees),
    path('delete/<id>', views.deleteEmployee),
    path('edit/<id>', views.editEmployee),
    path('update/<id>', views.updateEmployee)
]
