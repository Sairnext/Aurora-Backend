# Generated by Django 4.1.7 on 2023-05-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aurora_api', '0013_models_origin'),
    ]

    operations = [
        migrations.AddField(
            model_name='models',
            name='smart_funnel',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
