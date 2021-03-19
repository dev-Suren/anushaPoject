# Generated by Django 3.1.5 on 2021-01-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_employer', models.CharField(max_length=100)),
                ('job_position', models.CharField(max_length=200)),
                ('job_category', models.CharField(choices=[('finance', 'Finance'), ('marketing', 'Marketing'), ('webdesign', 'Webdesign'), ('accountant', 'Accountant')], default='finance', max_length=250)),
                ('job_description', models.TextField()),
                ('job_phone', models.CharField(max_length=100)),
                ('job_email', models.EmailField(max_length=254)),
                ('job_website', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Jobs',
        ),
    ]
