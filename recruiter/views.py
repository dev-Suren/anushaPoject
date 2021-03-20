from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        user = auth.authenticate(username=username, password=password1)
        if user is not None:
            client1=Client.objects.get(user=user)
            if(client1.userType == 'seeker'):
                auth.login(request, user)
                return redirect('seekerDashboard')
                auth.login(request, user)

            elif(client1.userType == 'superuser'):
                auth.login(request, user)
                return HttpResponseRedirect('admin')
                auth.login(request, user)
                
            else:
                auth.login(request, user)
                return redirect('landingpage')
                auth.login(request, user)


        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')