from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm
from .forms import UserRegistrationForm
from .models import Application
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm

from .forms import StatusUpdateForm

def home(request):
    return render(request,'home.html')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def cibil_calculator(request):
    return render(request, 'loans/cibil_calculator.html')


def about_us(request):
    return render(request, 'loans/about_us.html')




@login_required
def view_application(request, application_id):
    application = get_object_or_404(Application, id=application_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save(commit=False)
            # Here you can add ML prediction logic and update the status accordingly
            application.save()
            return redirect('admin_dashboard')
    else:
        form = ApplicationForm(instance=application)
    return render(request, 'loans/view_application.html', {'form': form, 'application': application})




@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('customer_dashboard')

    if request.method == 'POST':
        # Handle status update
        application_id = request.POST.get('application_id')
        application = get_object_or_404(Application, id=application_id)
        form = StatusUpdateForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = StatusUpdateForm()  # Default form

    applications = Application.objects.all()
    return render(request, 'loans/admin_dashboard.html', {'applications': applications, 'form': form})

@login_required
def customer_dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'loans/customer_dashboard.html', {'applications': applications})

@login_required
def apply_loan(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('customer_dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'loans/apply_loan.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('customer_dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('admin_dashboard')
                else:
                    return redirect('customer_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
