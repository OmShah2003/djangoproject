from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Patient, Doctor

class CustomUserCreationForm(UserCreationForm):
    address = forms.CharField(required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)

class PatientSignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        if commit:
            user.save()
            Patient.objects.create(user=user, address=self.cleaned_data.get('address'))
        return user

class DoctorSignUpForm(CustomUserCreationForm):
    class Meta(CustomUserCreationForm.Meta):
        model = CustomUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        if commit:
            user.save()
            Doctor.objects.create(user=user, address=self.cleaned_data.get('address'))
        return user
