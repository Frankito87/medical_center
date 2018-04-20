from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from mc.forms import UserForm, PatientForm, ContactForm, AppointmentForm, TreatmentForm
from django.contrib.auth.decorators import login_required
from .decorators import staff_member_required
from .models import Patient, Appointment, TreatmentHistory
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

# Create your views here.

def index(request):
    return render(request, 'mc/index.html')

def services(request):
    return render(request, 'mc/services.html')

def about(request):
    return render(request, 'mc/about.html')

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            phone_number = request.POST.get(
                'phone_number'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'phone_number': phone_number,
                'form_content': form_content
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')
    return render(request, 'mc/contact.html', {
        'form': form_class})

def register(request):
    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            user = f.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('index')
    else:
        f = UserForm()
    return render(request, 'mc/register.html', {'form': f})

def log_in(request):
    if request.method == 'POST':
        f = AuthenticationForm(data=request.POST)
        if f.is_valid():
            user = f.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('create_patient')
            else:
                return redirect('index')
    else:
        f = AuthenticationForm()
    return render(request, 'mc/log_in.html', {'form': f})

@staff_member_required
def create_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('patient_information', pk=post.pk)
    patients = Patient.objects.all()
    return render(request, 'mc/patient.html', {'patients': patients, 'form': PatientForm()})

@staff_member_required
def patient_information(request, pk):
    model = get_object_or_404(Patient, pk=pk)
    return render(
        request,
        'mc/patient_information.html',
        {'model': model}
    )

@staff_member_required
def update_patient(request, pk):
    model = get_object_or_404(Patient, pk=pk)
    form = PatientForm(instance=model)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=model)
        if form.is_valid():
            model = form.save()
            model.save()
            return redirect('patient_information', pk=model.pk)
    return render(request, 'mc/update.html', {'form': form})

@staff_member_required
def delete_patient(request, pk):
    if request.method == 'POST':
        model = get_object_or_404(Patient, pk=pk)
        model.delete()    
    return redirect('create_patient')

@staff_member_required    
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'mc/patient_list.html', {'patients': patients})

def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('appointment_information', pk=post.pk)
    appointments = Appointment.objects.all()
    return render(request, 'mc/create_appointment.html', {'appointments': appointments, 'form': AppointmentForm()})

def appointment_information(request, pk):
    model = get_object_or_404(Appointment, pk=pk)
    return render(
        request,
        'mc/appointment_information.html',
        {'model': model}
    )

@staff_member_required
def update_appointment(request, pk):
    model = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(instance=model)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=model)
        if form.is_valid():
            model = form.save()
            model.save()
            return redirect('appointment_information', pk=model.pk)
    return render(request, 'mc/update_appointment.html', {'form': form})

@staff_member_required
def delete_appointment(request, pk):
    if request.method == 'POST':
        model = get_object_or_404(Appointment, pk=pk)
        model.delete()    
    return redirect('create_appointment')

@staff_member_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'mc/appointment_list.html', {'appointments': appointments})

@staff_member_required    
def create_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('treatment_information', pk=post.pk)
    treatment = TreatmentHistory.objects.all()
    return render(request, 'mc/create_treatment.html', {'treatment': treatment, 'form': TreatmentForm()})

def treatment_information(request, pk):
    model = get_object_or_404(TreatmentHistory, pk=pk)
    return render(
        request,
        'mc/treatment_history.html',
        {'model': model})

@staff_member_required
def delete_treatment(request, pk):
    if request.method == 'POST':
        model = get_object_or_404(TreatmentHistory, pk=pk)
        model.delete()    
    return redirect('create_treatment')

@staff_member_required
def treatment_list(request):
    treatments = TreatmentHistory.objects.all()
    return render(request, 'mc/treatment_list.html', {'treatments': treatments})


def log_out(request):
    logout(request)
    return render(request, 'mc/index.html')


