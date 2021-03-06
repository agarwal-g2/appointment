# Generated by Django 3.2.5 on 2021-07-31 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appointment_booking.patient'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('SCHEDULED', 'scheduled'), ('COMPLETED', 'completed'), ('CANCELLED', 'cancelled')], default='SCHEDULED', max_length=20),
        ),
    ]
