from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import * 

def index(request):

	employees = Employee_model.objects.all().order_by('name')
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
