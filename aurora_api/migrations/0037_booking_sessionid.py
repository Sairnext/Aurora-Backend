# Generated by Django 4.1.7 on 2023-07-17 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0036_booking_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='sessionid',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
