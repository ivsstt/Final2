from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import EmployeeForm, RoleForm, TaskForm


def index(request):
    employees = Employee.objects.all()
    return render(request, 'index/index.html', locals())


def create_emp(request):
    error = ''
    if request.method == 'POST':
        f = EmployeeForm(request.POST)
        if Employee.objects.filter(name=request.POST['name']).exists():
            error = "Сотрудник с таким именем уже существует"
        else:
            f.save()
            return redirect('index')

    form = EmployeeForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'index/create_emp.html', context)


def roles(request):
    roles = Role.objects.all()
    return render(request, 'index/roles.html', locals())


def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'index/tasks.html', locals())


def create_role(request):
    error = ''
    if request.method == 'POST':
        f = RoleForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('roles')

    form = RoleForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'index/create_role.html', context)


def create_task(request):
    error = ''
    if request.method == 'POST':
        f = TaskForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('tasks')

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'index/create_task.html', context)


def delete_emp(request, emp_id):
    try:
        e = Employee.objects.filter(id=emp_id)
        e.delete()
        return redirect('index')
    except Employee.DoesNotExist:
        return HttpResponseNotFound("<h2>Сотрудник не найден</h2>")


def delete_role(request, r_id):
    try:
        r = Role.objects.filter(id=r_id)
        r.delete()
        return redirect('roles')
    except Role.DoesNotExist:
        return HttpResponseNotFound("<h2>Должность не найдена</h2>")


def delete_task(request, t_id):
    try:
        t = Task.objects.filter(id=t_id)
        t.delete()
        return redirect('tasks')
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Задача не найдена</h2>")


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'index/edit_task.html', {'form': form})


def edit_role(request, pk):
    role = get_object_or_404(Role, pk=pk)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roles')
    else:
        form = RoleForm(instance=role)
    return render(request, 'index/edit_role.html', {'form': form})


def edit_emp(request, pk):
    emp = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EmployeeForm(instance=emp)
    return render(request, 'index/edit_emp.html', {'form': form})
