from django.contrib import admin
from .models import User, Doctor, Appointment


admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Appointment)
# Register your models here.
