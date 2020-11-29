from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import * 

def index(request):

	return redirect('/employee-details')

def employee_details(request):
	
	employees = Employee_model.objects.all().order_by('name')
	form = Search_Form()

	context = {
		'employees' : employees,
		'form' : form
	}

	return render(request, 'employee/employee_details.html', context)


def enroll_employee(request):

	employees = Employee_model.objects.all()
	form = Employee_Form()

	if request.method == 'POST':
		form = Employee_Form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'employees' : employees,
		'form' : form
	}

	return render(request, 'employee/enroll_employee.html', context)

def update_employee_details(request, pk):

	employee = Employee_model.objects.get(id=pk)

	form = Employee_Form(instance=employee)

	if request.method == 'POST':
		form = Employee_Form(request.POST, instance=employee)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {
		'form': form
	}

	return render(request, 'employee/update_employee_details.html', context)


def delete_employee(request, pk):
	item = Employee_model.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {
		'item': item
	}
	
	return render(request, 'employee/delete.html', context)

def get_employee(request, pk):
	
	emp = Employee_model.objects.get(id=pk)

	context = {
		'emp': emp
	}
	
	return render(request, 'employee/employee.html', context)

def order_by(request, attr):


	employees = Employee_model.objects.all().order_by(attr)
	form = Employee_Form()

	if request.method == 'POST':
		form = Employee_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {
		'employees' : employees,
		'form' : form
	}

	return render(request, 'employee/employee_details.html', context)

def search_employee(request):

	form = Search_Form()

	if request.method == 'POST':
		form = Search_Form(request.POST)
		if form.is_valid():
			query = form.cleaned_data['name']
			queryset = Employee_model.objects.filter(name__icontains=query)
		# return redirect('/')

		context = {
			'employees' : queryset,
			'form' : form
		}

		return render(request, 'employee/employee_details.html', context)

	return redirect('/')