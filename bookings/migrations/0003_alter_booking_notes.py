# Generated by Django 3.2.21 on 2023-09-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_alter_booking_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='notes',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
