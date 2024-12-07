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

#Information for customer are stored as objects
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

#Information for pets are stored as objects
def pets(request):
    pets = Pet.objects.all()
    return render(request, 'pets.html', {'pets': pets})

#Tab for logging the user out
def logout_user(request):
	logout(request)
	messages.success(request, "Logged out successfully.")
	return redirect('home')

#Tab for registration of user or signing up
def register_user(request):
	if request.method == 'POST':
		#connects to the sign up form in forms.py
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#Authenticate and Login with valid credentials
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "Signed up successfully.")
			return redirect('home')
	else:
		#if not registered yet, the new user will be directed to registration form
		form = SignUpForm()
		return render(request, 'register.html', {'form': form})
	return render(request, 'register.html', {'form': form})

#Tab for viewing customer records table
def customer_record(request, pk):
	if request.user.is_authenticated:
		#look up an individual record
		customer_record = Customer.objects.get(id=pk)
		return render(request, 'records.html', {'customer_record':customer_record})
	else:
		messages.success(request, "You must be logged in to view that page")
		return redirect('home')

#Tab for viewing pet records table
def pet_record(request, pk):
	if request.user.is_authenticated:
		#look up an individual pets record
		pet_record = Pet.objects.get(id=pk)
		return render(request, 'pet_records.html', {'pet_record':pet_record})
	else:
		messages.success(request, "You must be logged in to view that page")
		return redirect('home')

#Deletion of pet record as a button
def delete_pet(request, pk):
	if request.user.is_authenticated:
		delete_p = Pet.objects.get(id=pk)
		delete_p.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, "You Must be Logged in to complete action.")
		return redirect('home')

#Adding a new pet record
def add_pet(request):
    form_p = AddPetForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form_p.is_valid():
				#access forms.py for adding pet records
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

#Deletion of Customer record as a button
def delete_customer(request, pk):
	if request.user.is_authenticated:
		delete_it = Customer.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully")
		return redirect('home')
	else:
		messages.success(request, "You Must be Logged in to complete action.")
		return redirect('home')
	
#Adding of customer record
def add_customer(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			#access forms.py for adding new customer record
			if form.is_valid():
				form.save()
				messages.success(request, "Successfully added record.")
				return redirect('customers')

		return render(request, 'add_customer.html', {'form': form})
	else:
		messages.success(request, "You must be logged in.")
		return redirect('home')

#Button for updating customer record
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

#Button for updating pet record
def update_pet(request, pk):
    if request.user.is_authenticated:
        # Get the current customer record or return a 404 if not found
        current_pet = get_object_or_404(Pet, id=pk)

        # If the request is POST, handle form submission
        if request.method == "POST":
            form_p = AddPetForm(request.POST, instance=current_pet)
            if form_p.is_valid():
                form_p.save()
                messages.success(request, "Pet record updated successfully.")
                return redirect('pet_record', pk=pk)  # Redirect to the pet record page
        else:
            # For GET requests, display the form prefilled with the current customer data
            form_p = AddPetForm(instance=current_pet)

        return render(request, 'update_pet.html', {'form_p': form_p})

    else:
        messages.error(request, "You must be logged in to update a customer record.")
        return redirect('home')