# Generated by Django 3.1.6 on 2021-03-20 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210320_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterdetails',
            name='contactNumber',
            field=models.CharField(max_length=30, null=True),
        ),
    ]