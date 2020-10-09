from django.urls import path
from .department.views import *
from .employee.views import *


urlpatterns = [
    path('', department_list, name='department_list_url'),
    path('create/', department_create, name='create_department_url'),
    path('<int:department_id>/delete/', department_delete, name='department_delete_url'),
    path('<int:department_id>/edit/', department_edit, name='department_edit_url'),
    path('<int:department_id>/employee_list', employee_list, name='employee_list_url')
]