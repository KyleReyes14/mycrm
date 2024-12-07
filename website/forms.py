from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer, Pet

#Registration form to be answered by user to create an account
class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
	first_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
	last_name = forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    
	class Meta:
        #name of fields to be filled up by new user
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
        #account for attributes and data type to be placed in form placeholders

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        #First password
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
		
        #Retyping of password to confirm no typographical errors
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


#Add customer record form based on the migrated models
class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}),
        label=""
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}),
        label=""
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}),
        label=""
    )
    phone = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "form-control"}),
        label=""
    )
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Address", "class": "form-control"}),
        label=""
    )
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "City", "class": "form-control"}),
        label=""
    )
    prospect = forms.ModelChoiceField(
          queryset=Pet.objects.all(),
          widget=forms.Select(attrs={'class':'form-control'}),
          required=False
    )
    #date data type for the time of inquiry of customer
    inquire_date = forms.DateField(
        required=False,  # Optional if not always needed
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Inquire Date"
    )

    #date data type for the time of concluded settlement of customer
    approved_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Approved Date"
    )
    class Meta:
        model = Customer  # Specify the model here
        fields = ['first_name', 'last_name', 'email', 'phone', 
                'address', 'city', 'prospect', 'inquire_date', 
                'approved_date']
		
#add pet record form based on the pet migrated models
class AddPetForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}),
        label=""
    )
    species = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Species", "class": "form-control"}),
        label=""
    )
    breed = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Breed", "class": "form-control"}),
        label=""
    )
    age = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={"placeholder": "Age", "class": "form-control"}),
        label=""
    )
    description = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Description", "class": "form-control"}),
        label=""
    )
    #choice field for status of adoption
    adopted = forms.ChoiceField(
        choices=Pet.status_choices,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Adopted Status"
    )
    #choice field for name of existing or prospect owner
    owner = forms.ModelChoiceField(
    queryset=Customer.objects.all(), 
    widget=forms.Select(attrs={"class": "form-control"}), 
    required=False,  # Makes the field optional
    empty_label="No Owner"  # Adds a blank option with this label
    )
    class Meta:
        model = Pet  # Specify the model here
        fields = ['name','species', 'breed', 'age', 'description', 'adopted', 'owner']
