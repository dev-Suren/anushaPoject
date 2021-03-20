from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recruiterHome(request):
	return HttpResponse('THis is recruiter dashboard')

