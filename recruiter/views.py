from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import *

# Create your views here.
def recruiterHome(request):
	userdata = recruiterDetails.objects.filter(user=request.user)
	return render(request, 'landingpage.html',{'userdata': userdata})

