# Generated by Django 4.1.7 on 2023-07-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0034_booking_calendar_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
