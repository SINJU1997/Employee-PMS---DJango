from django.db import models

# Create your models here.
class Employee(models.Model):
    Name=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    Phoneno=models.CharField(max_length=20)
    Designation=models.CharField(max_length=100)