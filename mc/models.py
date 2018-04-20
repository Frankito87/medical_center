from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model):
    SEXES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    CONTACT = (
        ('voice', 'Voice'),
        ('text', 'Text'),
    )

    first_name = models.CharField(max_length=150)
    mi = models.CharField(max_length=128)
    last_name = models.CharField(max_length=150)
    previous_name = models.CharField(max_length=150)
    mailing_address = models.CharField(max_length=150)
    city_state_code = models.CharField(max_length=128)
    home_phone = models.CharField(max_length=15)
    cell_phone = models.CharField(max_length=15)
    work_phone = models.CharField(max_length=15)
    method_contact = models.CharField(max_length=5, choices=CONTACT)
    date_birth = models.DateField(max_length=8)
    age = models.IntegerField()
    gender = models.CharField(max_length=8, choices=SEXES)
    emergency_contact = models.CharField(max_length=128)
    emergency_contact_phone = models.CharField(max_length=15)
    relationship = models.CharField(max_length=128)
    created = models.DateField()
    insurance = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.mailing_address} by {self.cell_phone}'  

class Appointment(models.Model):
    name = models.CharField(max_length=128)  
    phone_number = models.CharField(max_length=15)
    category = models.CharField(max_length=128)
    doctor = models.CharField(max_length=128)
    created = models.DateTimeField()      
    
    def __str__(self):
        return f'{self.category}  {self.doctor}  {self.created} by {self.name}'

class TreatmentHistory(models.Model):
    treatment = models.CharField(max_length=128)
    notes = models.CharField(max_length=128)
    date = models.DateField()
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.treatment}  {self.notes}  {self.date} by {self.Appointment.id}'



