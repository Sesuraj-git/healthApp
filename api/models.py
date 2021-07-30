from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User as usr
from django.db import models
import datetime
from .validators import valid_mob


# Create your models here.
class User(usr):
    is_doctor = models.BooleanField(blank=False)
    phone = models.CharField(max_length=16, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, default=datetime.date.today())
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=Gender_choices, blank=True)


class Doctor(models.Model):
    is_available = models.BooleanField(default=True)
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    doc_mobile = models.CharField(max_length=10, validators=[valid_mob], blank=False)
    doc_spec = models.CharField(max_length=20, blank=True)
    has_appointments = models.IntegerField(blank=True)

    def has_appointment(self):
        appointments = Appointment.objects.filter(doctor=self, status=False)
        print(appointments)
        self.has_appointments = len(appointments)
        return len(appointments)

    def __str__(self):
        return str(self.user.username)


class Appointment(models.Model):
    patient = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,null=True, on_delete=models.SET_NULL)
    appointment_date = models.DateField(null=False, auto_now=datetime.date.today())
    status = models.BooleanField(default=False)

    def patientName(self):
        return self.patient.full_name

    def __str__(self):
        return str(self.doctor)
