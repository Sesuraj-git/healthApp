from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Doctor, Appointment
from .serializers import UserSerializer, DoctorSerializer, AppointmentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        doctor = Doctor.objects.all()
        doctor = doctor.order_by('has_appointments')[0]

    def create(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user)
        doctor = Doctor.objects.all()
        doctor = doctor.order_by('has_appointments')[0]
        appointment = Appointment.objects.create(patient=user, doctor=doctor)

        appointment.doctor = doctor
        appointment.save()
        serializer = AppointmentSerializer(appointment, many=False)
        response = {'Appointments': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(patient=user)
        doctor = Doctor.objects.get(user=user)
        if user.is_doctor:
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            response = {'doctor': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            appointments = Appointment.objects.filter(user=user)
            serializer = AppointmentSerializer(appointments, many=True)
            response = {'doctor': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        print(request.data)
        user = User.objects.get(username=request.user)
        if user.is_doctor:
            doc_mobile = request.data['doc_mobile']
            doc_spec = request.data['doc_spec']
            doctor = Doctor.objects.create(user=user, doc_mobile=doc_mobile, doc_spec=doc_spec)
            print(doctor)

            serializer = DoctorSerializer(doctor, many=False)
            response = {'doctor': serializer.data}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'Message': "you are not assigned as doctor"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
