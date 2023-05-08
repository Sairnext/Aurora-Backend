# Generated by Django 4.1.7 on 2023-05-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0011_alter_models_credentials_alter_models_tokens'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='models',
            name='credentials',
        ),
        migrations.AlterField(
            model_name='models',
            name='tokens',
            field=models.FileField(max_length=200, null=True, upload_to='tokens'),
        ),
        migrations.AlterField(
            model_name='models',
            name='training_file',
            field=models.FileField(null=True, unique=True, upload_to='training_file'),
        ),
    ]