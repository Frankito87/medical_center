# Generated by Django 2.0.3 on 2018-04-12 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mc', '0007_auto_20180411_2036'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='date',
            new_name='created',
        ),
    ]
