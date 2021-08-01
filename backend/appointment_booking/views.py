import logging

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import routers, serializers, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Appointment, Patient, Book
from .serializers import AppointmentSerializer, PatientSerializer, BookSerializer

logger = logging.getLogger(__name__)

# ViewSets define the view behavior.
# https://www.django-rest-framework.org/api-guide/viewsets/#viewsets


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related('patient','appointment').all()
    serializer_class = BookSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    @action(detail=True, methods=["patch"])
    def book(self, request, pk=None):
        appointment = Appointment.objects.get(pk=pk)
        patient = Patient.objects.get(pk=request.data.get("patient_pk"))
        logger.info("Booking appointment %s for patient %s", appointment.pk, patient.pk)
        # TODO: implement appointment booking logic
        # Check if the appointment is already booked
        if self.get_book_by_appointment(appointment) :
            return Response("Appointment is already booked, please try for some other appointment.", status=status.HTTP_409_CONFLICT)

        book = Book.objects.create(
            patient = patient,
            appointment = appointment
        )

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_book_by_appointment(self, appointment):
        book = Book.objects.filter(
            appointment = appointment,
            status = "SCHEDULED"
        )

        return True if book else False