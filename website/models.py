from django.db import models

# Create your models here.
class Customer(models.Model):
	# Fields for Customer information
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length=15, blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.first_name} {self.last_name}"

class Pet(models.Model):
	# Fields for Pet information
	status_choices = [
		('Approved', 'Approved'),
		('Pending', 'Pending'),
		('Rejected', 'Rejected'),
		('No Proespect Yet', 'No Prospect Yet'),
	]

	name = models.CharField(max_length=100)
	species = models.CharField(max_length=50)  # e.g., Dog, Cat
	breed = models.CharField(max_length=100, blank=True, null=True)
	age = models.IntegerField()
	description = models.TextField(blank=True, null=True)
	adopted = models.CharField(
        max_length=25,
        choices=status_choices,
        default='Pending'
	  )  # Status of adoption process
	owner = models.ForeignKey(
		Customer, on_delete=models.SET_NULL, blank=True, null=True,
		related_name='pets'  # Reverse lookup for customer's pets
	)	#as a pet might not have an owner yet