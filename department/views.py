from django.shortcuts import render, redirect, reverse
from .models import Department
from django.views.decorators.http import require_http_methods
from .forms import DepartmentForm
from .services import *


@require_http_methods(['GET'])
def department_list(request):
    department_data = department_list_function()
    return render(request,
                  'department/department_list_.html',
                  context={'department_data': department_data})


@require_http_methods(['GET', 'POST'])
def department_create(request):
    bound_form = DepartmentForm(request.POST or None)
    if request.method == 'POST' and bound_form.is_valid():
        bound_form.save()
        return redirect(reverse('department_list_url'))

    return render(request, 'department/create_department.html', context={'form': bound_form})


@require_http_methods(['GET', 'POST'])
def department_edit(request, department_id):
    department = Department.objects.get(id=department_id)
    bound_form = DepartmentForm(request.POST or None, instance=department)
    if request.method == 'POST' and bound_form.is_valid():
        add_department_function(bound_form)
        return redirect(reverse('department_list_url'))

    return render(request, 'department/department_edit.html',
                  context={'form': bound_form,
                           'department': department})


@require_http_methods(['GET'])
def department_delete(request, department_id):
    delete_department_function(department_id)
    return redirect(reverse('department_list_url'))



