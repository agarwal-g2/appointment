# Generated by Django 3.0 on 2020-04-18 18:30

from django.db import migrations


def seed_clinician_availabilities(apps, schema_editor):
    Clinician = apps.get_model("clinicians", "Clinician")
    Availability = apps.get_model("availabilities", "Availability")

    availability_1 = Availability.objects.first()
    cynthia = Clinician.objects.filter(national_provider_identifier="1234567890").first()
    cynthia.availabilities.add(availability_1)

    availability_2 = Availability.objects.get(pk=2)
    carl = Clinician.objects.filter(national_provider_identifier="0987654321").first()
    carl.availabilities.add(availability_2)

    availability_4 = Availability.objects.get(pk=4)
    cynthia.availabilities.add(availability_4)
    carl.availabilities.add(availability_4)

    availability_5 = Availability.objects.get(pk=5)
    carl.availabilities.add(availability_5)


class Migration(migrations.Migration):

    dependencies = [
        ("clinicians", "0002_auto_20200418_1821"),
        ("availabilities", "0002_auto_20200418_1807"),
    ]

    operations = [
        migrations.RunPython(seed_clinician_availabilities),
    ]
