# Generated by Django 5.0.7 on 2025-02-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_rename_booking_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='customer_id',
            field=models.IntegerField(default=None),
        ),
    ]
