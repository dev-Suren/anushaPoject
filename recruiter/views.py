from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recruiterHome(request):
	return render(request, 'landingpage.html')

