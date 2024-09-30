from rest_framework import serializers
from .models import Doctor, Patient, Appointment
from datetime import datetime

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone_number",
            "email"
        ]


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "phone_number",
            "email",
            "address"
        ]

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]

class CreateUpdateAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = [
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]

    def validate(self, value):
        dt = datetime.combine(value["date"], value["at_time"])
        if dt < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return value

    def validate_doctor(self, value):
        if not Doctor.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Doctor does not exist")
        return value
    
    def validate_patient(self, value):
        if not Patient.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Patient does not exist")
        return value
        
