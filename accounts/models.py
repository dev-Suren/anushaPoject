from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):    
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    gender = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=50, null=True)
    interestedIN = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.user.username



class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job_id = models.AutoField(primary_key=True, null=False)
    JOB_CHOICES = (
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('webdesign', 'Webdesign'),
        ('accountant', 'Accountant'),
        ('others', 'Others')
    )
    job_title = models.CharField(max_length=200)
    job_employer = models.CharField(max_length=100)
    job_position = models.CharField(max_length=200)
    job_category = models.CharField(max_length=250, choices=JOB_CHOICES, default='others')
    job_description = models.TextField()
    job_phone = models.CharField(max_length=100)
    job_email = models.EmailField()
    job_website = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.job_title


class SavedJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)


class AppliedJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, blank=True, null=True)


class recruiterDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    contactNumber = models.CharField(max_length=30,null=True)
    Location = models.CharField(max_length=15, null=True)
    CompanyEmail = models.CharField(max_length=15, null=True)
    CompanyType = models.CharField(max_length=15, null=True)
    CompanyName = models.CharField(max_length=15, null=True)
    CompanyContact = models.CharField(max_length=15, null=True)
    personalName = models.CharField(max_length=15, null=True)
    personalContact = models.CharField(max_length=15, null=True)

    def __str__(self):
        return self.user.Username
    


class UserDataTypes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    userTypes = models.CharField(max_length=15,null=True)
    def __str__(self):
        return self.user.Username


