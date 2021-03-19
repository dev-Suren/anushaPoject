from django.shortcuts import render

# Create your views here.
def addJob(request):
	return render(request,'jobForm.html')