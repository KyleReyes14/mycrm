from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm, AddPetForm
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
	
def pet_record(request, pk):
	if request.user.is_authenticated:
		#look up indiv pets record
		pet_record = Pet.objects.get(id=pk)
		return render(request, 'pet_records.html', {'pet_record':pet_record})
	else:
		messages.success(request, "You must be logged in to view that page")
		return redirect('home')

def delete_pet(request, pk):
	if request.user.is_authenticated:
		delete_p = Pet.objects.get(id=pk)
		delete_p.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, "You Must be Logged in to complete action.")
		return redirect('home')

def add_pet(request):
    form_p = AddPetForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form_p.is_valid():
                print("Form is valid. Saving...")
                form_p.save()
                messages.success(request, "Successfully added record.")
                return redirect('pets')
            else:
                print("Form is invalid:", form_p.errors)  # Log errors
        return render(request, 'add_pet.html', {'form_p': form_p})
    else:
        messages.success(request, "You must be logged in.")
        return redirect('home')

def delete_customer(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, "You Must be Logged in to complete action.")
		return redirect('home')

def add_customer(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				form.save()
				messages.success(request, "Successfully added record.")
				return redirect('customers')

		return render(request, 'add_customer.html', {'form': form})
	else:
		messages.success(request, "You must be logged in.")
		return redirect('home')

def update_customer(request, pk):
    if request.user.is_authenticated:
        # Get the current customer record or return a 404 if not found
        current_customer = get_object_or_404(Customer, id=pk)

        # If the request is POST, handle form submission
        if request.method == "POST":
            form = AddRecordForm(request.POST, instance=current_customer)
            if form.is_valid():
                form.save()
                messages.success(request, "Customer record updated successfully.")
                return redirect('record', pk=pk)  # Redirect to the customer record page
        else:
            # For GET requests, display the form prefilled with the current customer data
            form = AddRecordForm(instance=current_customer)

        return render(request, 'update_customer.html', {'form': form})

    else:
        messages.error(request, "You must be logged in to update a customer record.")
        return redirect('home')