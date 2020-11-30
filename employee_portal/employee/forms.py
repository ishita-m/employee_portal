from django import forms
from django.forms import ModelForm
from .models import *

class Employee_Form(forms.ModelForm):

	# name = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'eg. Daniel Redcliff'}))
	# location = forms.CharField(widget= forms.Textarea(attrs={'placeholder':'eg. Chennai'}))
	# phone_number = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder':'eg. 911234554321'}))
	# email_id = forms.EmailField()
	# joining_date = forms.DateField()
	# last_date = forms.DateField()

	class Meta:
		model = Employee_model
		fields = '__all__'

	# def clean_email_id(self):
	# 	email_id_passed = self.cleaned_data.get("email_id")
	# 	if not "gmail.com" in email_id_passed:
	# 		raise forms.ValidationError("Please enter a valid email id.")
	# 	return email_id_passed

	def clean_phone_number(self):
		phone_number_passed = self.cleaned_data.get("phone_number")
		if len(str(phone_number_passed)) != 10:
			raise forms.ValidationError("Please enter valid 10 digit phone number.")
		return phone_number_passed


class Search_Form(forms.ModelForm):

	class Meta:
		model = Employee_model
		fields = ['name']