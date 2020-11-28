from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "list"),
	path('enroll/employee', views.enroll_employee, name = "enroll"),
]  