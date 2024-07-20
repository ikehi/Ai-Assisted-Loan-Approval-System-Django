from django import forms
from .models import Application
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ApplicationForm(forms.ModelForm):
    EMPLOYMENT_STATUS_CHOICES = [
        (0, 0),
        (1, 1),
    ]

    employment_status = forms.ChoiceField(
        choices=EMPLOYMENT_STATUS_CHOICES,
        help_text="0 is for unemployed and 1 is for employed",
        widget=forms.Select
    )
    class Meta:
        model = Application
        fields = [
            'passport_photo','name', 'age', 'contact_no', 'city', 'cibil_score', 'income',
            'employment_status', 'loan_term', 'loan_amount',
            'residential_assets', 'commercial_assets'
        ]


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=Application.STATUS_CHOICES)
        }

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