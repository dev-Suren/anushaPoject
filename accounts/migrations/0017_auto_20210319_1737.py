# Generated by Django 3.1.6 on 2021-03-19 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0016_remove_recruiterdetails_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterdetails',
            name='personalEmail',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='recruiterdetails',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
