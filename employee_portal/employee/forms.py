from django import forms
from django.forms import ModelForm
from .models import *

class Employee_Form(forms.ModelForm):

	# name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'eg. Daniel Redcliff'}))
	# location = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'eg. Chennai'}))
	# phone_number = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder':'eg. 911234554321'}), max_length=12)
	# email_id = forms.EmailField(max_length = 200)
	# joining_date = forms.DateField()
	# last_date = forms.DateField()
	
	class Meta:
		model = Employee_model
		fields = '__all__'

class Search_Form(forms.ModelForm):

	class Meta:
		model = Employee_model
		fields = ['name']