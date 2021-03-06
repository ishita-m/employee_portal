from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = "list"),
	path('employee-details', views.employee_details, name = "employee_details"),
	path('enroll/employee', views.enroll_employee, name = "enroll"),
	path('update_employee_details/<str:pk>/', views.update_employee_details	, name = "update_emp"),
	path('delete/<str:pk>/', views.delete_employee, name = "delete"),
	path('employee/<str:pk>/', views.get_employee, name = "employee_data"),
	path('order_by/<str:attr>/', views.order_by, name = "order_by"),
	path('search_results', views.search_employee, name = "search_employee"),
]  