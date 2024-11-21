from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Customer, Pet

# Create your views here.
def home(request):
	customers = Customer.objects.all()
	
	#authentication of logging in 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#Authenticate
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, "You've logged in!")
			return redirect('home')
		else:
			messages.success(request, "Please check your login credentials and Try again.")
			return redirect('home')
	else: 
		return render(request, 'home.html', {})

def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets.html', {'pets': pets})

def logout_user(request):
	logout(request)
	messages.success(request, "Logged out successfully.")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#Authenticate and Login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Signed up successfully.")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		#look up indiv record
		customer_record = Customer.objects.get(id=pk)
		return render(request, 'records.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to view that page")
		return redirect('home')
	
def delete_customer(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Records Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, "You Must be Logged in to complete action.")
		return redirect('home')