from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Application
from .forms import ApplicationForm, UserRegistrationForm, StatusUpdateForm
import tensorflow as tf
from sklearn.preprocessing import StandardScaler
import numpy as np
import joblib

# Load your ANN model
model_path = "ann_model.h5"

model = tf.keras.models.load_model(model_path)

scaler_path = "scaler.pkl"

scaler = joblib.load(scaler_path)


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def cibil_calculator(request):
    return render(request, 'loans/cibil_calculator.html')


def about_us(request):
    return render(request, 'loans/about_us.html')


@login_required
def view_application(request, application_id):
    print("view_application function called")
    application = get_object_or_404(Application, id=application_id)

    if request.method == 'POST':
        print('Entered')
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            application = form.save(commit=False)
            application.save()
            return redirect('admin_dashboard')
    else:
        print('else')
        form = ApplicationForm(instance=application)

    # Prepare input data for the model
    input_data = np.array([[
        application.no_of_dependents,
        application.education,
        application.employment_status,
        application.income_annum,
        application.loan_amount,
        application.loan_term,
        application.cibil_score,
        application.residential_assets_value,
        application.commercial_assets_value,
        application.luxury_assets_value,
        application.bank_asset_value
    ]])

    print("Input Data for Model Prediction:", input_data)

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)
    print("Scaled Input Data for Model Prediction:", input_data_scaled)

    # Make a prediction
    prediction = model.predict(input_data_scaled)

    # Get the prediction confidence
    # Since model.predict returns a list of lists
    prediction_confidence = prediction[0][0]

    # Assuming binary classification (0 or 1)
    prediction_status = "Approved" if prediction_confidence < 0.5 else "Rejected"

    # Calculate the confidence percentage
    confidence_percentage = prediction_confidence * \
        100 if prediction_status == "Rejected" else (
            1 - prediction_confidence) * 100

    # Create the prediction text
    prediction_text = (
        f"The prediction for applicant {application.name} by the ML model is {prediction_status} "
        f"with {confidence_percentage:.2f}% confidence."
    )

    # Save the prediction text to the application
    application.ml_prediction = prediction_text
    print("Prediction:", prediction)
    print("Prediction Confidence:", prediction_confidence)

    application.save()

    # Prepare context for rendering
    context = {
        'form': form,
        'application': application,
    }

    return render(request, 'loans/view_application.html', context)


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
