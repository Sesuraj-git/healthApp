from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet,  DoctorViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
# router.register('patients', PatientViewSet)
router.register('doctors', DoctorViewSet)
router.register('appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]