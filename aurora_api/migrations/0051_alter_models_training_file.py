# Generated by Django 4.1.7 on 2023-10-12 16:16

import aurora_api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0050_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='training_file',
            field=aurora_api.models.S3FileField(null=True, unique=True, upload_to='upload_to'),
        ),
    ]
