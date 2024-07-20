from django import forms
from .models import Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ApplicationForm(forms.ModelForm):
    EDUCATION_CHOICES = [
        (0, '0'),
        (1, '1'),
    ]
    
    EMPLOYMENT_STATUS_CHOICES = [
        (0, '0'),
        (1, '1'),
    ]

    education = forms.ChoiceField(
        choices=EDUCATION_CHOICES,
        help_text="0 for Graduate, 1 for Not Graduate",
        widget=forms.Select
    )

    employment_status = forms.ChoiceField(
        choices=EMPLOYMENT_STATUS_CHOICES,
        help_text="0 for Not Employed, 1 for Employed",
        widget=forms.Select
    )
    
    name = forms.CharField(
        max_length=100,
        help_text="Enter your full name",
    )

    contact_no = forms.CharField(
        max_length=15,
        help_text="Enter your contact number",
    )

    city = forms.CharField(
        max_length=100,
        help_text="Enter the city where you reside",
    )
    
    country = forms.CharField(
        max_length=100,
        help_text="Enter your country",
    )

    class Meta:
        model = Application
        fields = [
            'passport_photo', 'name', 'contact_no', 'city', 'country', 'no_of_dependents', 
            'education', 'employment_status', 'income_annum', 'loan_amount', 'loan_term', 
            'cibil_score', 'residential_assets_value', 'commercial_assets_value', 
            'luxury_assets_value', 'bank_asset_value'
        ]
        widgets = {
            'self_employed': forms.CheckboxInput,
        }

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']
        

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None