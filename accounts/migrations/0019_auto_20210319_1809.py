# Generated by Django 3.1.6 on 2021-03-19 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_recruiterdetails_usertypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruiterdetails',
            name='CompanyEmail',
        ),
        migrations.RemoveField(
            model_name='recruiterdetails',
            name='CompnayName',
        ),
        migrations.RemoveField(
            model_name='recruiterdetails',
            name='contactNumber',
        ),
        migrations.RemoveField(
            model_name='recruiterdetails',
            name='personalEmail',
        ),
    ]
