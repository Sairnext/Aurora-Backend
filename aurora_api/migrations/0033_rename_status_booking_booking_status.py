# Generated by Django 4.1.7 on 2023-06-30 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0032_booking_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='status',
            new_name='booking_status',
        ),
    ]