from django.db import models
from depapp.department.models import Department


class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    hire_date = models.DateField(auto_now=True)
