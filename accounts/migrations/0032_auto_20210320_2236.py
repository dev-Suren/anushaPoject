# Generated by Django 3.1.6 on 2021-03-20 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20210320_2200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='userType',
            new_name='userTypes',
        ),
    ]