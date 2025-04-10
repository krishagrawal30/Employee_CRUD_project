from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import Employeeform

def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/emp_list.html', {'employees' : employees})
def add_emp(request):
    if request.method == 'POST':
        form = Employeeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employeeform()
    return render(request, 'employees/employee_form.html', {'form': form})
def edit_emp(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        form = Employeeform(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emp_list')
    else:
        form = Employeeform(instance=employee)
    return render(request, 'employees/employee_form.html', {'form': form})
def delete_emp(request, id):
    employee = get_object_or_404(Employee, pk=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('emp_list')
    return render(request, 'employees/delete.html', {'employee': employee})