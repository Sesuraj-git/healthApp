from abc import ABC

from rest_framework import serializers
from .models import User, Doctor, Appointment
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_doctor')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        print(user, 'is created as doctor')
        return user


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        user = UserSerializer
        fields = ('is_available', 'user', 'doc_mobile', 'doc_spec','has_appointment','has_appointments')


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('id', 'patient', 'doctor', 'appointment_date', 'status')


