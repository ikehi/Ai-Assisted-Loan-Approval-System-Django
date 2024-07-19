from django import forms
from .models import Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            'name', 'age', 'contact_no', 'city', 'cibil_score', 'income',
            'employment_status', 'loan_term', 'loan_amount',
            'residential_assets', 'commercial_assets'
        ]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']