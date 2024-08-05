from django.db import models
from django.contrib.auth.models import User

# Extend the User model to include ServiceProviders
class ServiceProvider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

# Service model to represent different services offered by the service providers
class Service(models.Model):
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} by {self.service_provider.name}"

class ServiceCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    services = models.ManyToManyField(Service)

    def __str__(self):
        return self.name

# New Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

# Appointment model to represent appointments booked by users
class Appointment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment of {self.customer.name} with {self.service.service_provider.name} on {self.appointment_date} at {self.appointment_time}"
    
