# Generated by Django 2.0.3 on 2018-04-18 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0010_patient_insurance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='sex',
            new_name='gender',
        ),
    ]