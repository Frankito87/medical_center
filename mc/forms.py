from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Patient, Appointment, TreatmentHistory

class UserForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15)
    content = forms.CharField(required=True, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Full Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['phone_number'].label = "Phone Number"
        self.fields['content'].label = "How can we assist you?"

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

class TreatmentForm(ModelForm):
    class Meta:
        model = TreatmentHistory
        fields = '__all__'