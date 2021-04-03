from django import forms
from .models import Job,Client
from django.forms import ModelForm

class JobForm(forms.ModelForm):
    JOB_CHOICES = (
        ('finance', 'Finance'),
        ('marketing', 'Marketing'),
        ('webdesign', 'Webdesign'),
        ('accountant', 'Accountant'),
        ('others', 'Others')
    )
    # user = forms.CharField(label='')
    job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    job_employer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    job_position = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    job_category = forms.CharField(widget=forms.Select(choices=JOB_CHOICES, attrs={'class': 'form-input'}))
    job_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-input'}))
    job_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}))
    job_email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-input'}))
    job_website = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-input'}))
   
    
    class Meta:
        model = Job
        fields = '__all__'
        # fields = ['job_title', 'job_employer', 'job_position', 'job_category', 'job_description' ,'job_phone' ,'job_email','job_website']

class ClientForm(ModelForm):
    class Meta:
        model= Client
        fields = '__all__'
        #fields = ['contact','gender','address','education','interestedIN','cvImages']
