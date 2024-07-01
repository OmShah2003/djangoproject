'''from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import CustomUser

def home(request):
    return render(request, 'myapp/home.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print(f"New user created: {user.username}, email: {user.email}")  # Debug print
            if user.is_patient:
                return redirect('patient_dashboard')
            elif user.is_doctor:
                return redirect('doctor_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})

def user_profile(request):
    user = request.user  # Get the current logged-in user
    context = {
        'user': user
    }
    return render(request, 'user_profile.html', context)
'''

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import PatientSignUpForm, DoctorSignUpForm
from .models import CustomUser

def signup(request):
    return render(request, 'signup.html')

def patient_signup(request):
    if request.method == 'POST':
        form = PatientSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = PatientSignUpForm()
    return render(request, 'signup_form.html', {'form': form, 'user_type': 'Patient'})

def doctor_signup(request):
    if request.method == 'POST':
        form = DoctorSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = DoctorSignUpForm()
    return render(request, 'signup_form.html', {'form': form, 'user_type': 'Doctor'})

@login_required
def patient_dashboard(request):
    return render(request, 'patient_dashboard.html')

@login_required
def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html')
