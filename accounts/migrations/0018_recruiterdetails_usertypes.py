# Generated by Django 3.1.6 on 2021-03-19 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210319_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiterdetails',
            name='userTypes',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
