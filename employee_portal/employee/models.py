from django.db import models

# Create your models here.
class Employee_model(models.Model):
	
	# id is auto generated
	name = models.CharField(max_length=100)
	location = models.TextField()
	phone_number = models.IntegerField()
	email_id = models.EmailField(max_length = 254)
	joining_date = models.DateField()
	last_date = models.DateField()

	def __str__(self):
		return self.name
