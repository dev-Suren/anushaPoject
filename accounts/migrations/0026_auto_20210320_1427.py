# Generated by Django 3.1.6 on 2021-03-20 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_recruiterdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='education',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='interestedIN',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='recruiterdetails',
            name='CompanyContact',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='recruiterdetails',
            name='CompnayEmail',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
