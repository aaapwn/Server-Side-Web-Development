from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=150)
    specialization = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'Dr. {self.name} ({self.specialization})'


class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    at_time = models.TimeField()
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Appointment with Dr. {self.doctor.name} for {self.patient.name} on {self.date.strftime("YYYY-MM-DD HH:mm")}'
