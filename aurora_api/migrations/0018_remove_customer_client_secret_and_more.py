# Generated by Django 4.1.7 on 2023-06-12 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0017_customer_client_secret'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='client_secret',
        ),
        migrations.AddField(
            model_name='customer',
            name='client_secret_file',
            field=models.FileField(null=True, unique=True, upload_to='secrets_file'),
        ),
    ]
