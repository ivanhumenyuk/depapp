from .models import Department
from .forms import *


def department_list_function():
    department_data = Department.objects.all()
    return department_data


def delete_department_function(department_id):
    department = Department.objects.get(id=department_id)
    department.delete()


def add_department_function(form):
    form.save()
