# Generated by Django 3.1.6 on 2021-04-01 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0037_auto_20210401_0311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='image',
        ),
    ]
