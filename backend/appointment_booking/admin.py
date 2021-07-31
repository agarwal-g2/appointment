from django.contrib import admin

from .models import Appointment, Patient, Book

admin.site.register(Appointment)
admin.site.register(Patient)
admin.site.register(Book)
