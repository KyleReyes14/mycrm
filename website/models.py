from django.db import models

# Create your models here.
# Create your models here.

# Fields for Pet information
class Pet(models.Model):
    #status choices for dropdown field choice on adoption status
    status_choices = [
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
        ('No Prospect Yet', 'No Prospect Yet'),
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
        'Customer', on_delete=models.SET_NULL, blank=True, null=True,
        related_name='pets'  # Reverse lookup for customer's pets
    )  # as a pet might not have an owner yet

    def __str__(self):
        return self.name  # Display the name of the pet in dropdowns

# Fields for Customer information
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    prospect = models.ForeignKey(
        'Pet', on_delete=models.SET_NULL, 
        blank=True, null=True, related_name='customers'
    ) # Reverse lookup for pets 
    inquire_date = models.DateTimeField(blank=True, null=True) #date data type for inquiry date
    approved_date = models.DateTimeField(blank=True, null=True) #date data type for concluded approved date

    def __str__(self):
        return f"{self.first_name} {self.last_name}" #displays concatenated string for first and last name