# Generated by Django 4.1.7 on 2023-07-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0035_customer_email_customer_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
