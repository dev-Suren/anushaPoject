from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages, auth
from .forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact = request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        username = request.POST['username']
        gender = request.POST['gender']
        userType = request.POST['userType']

        if password1 != password2:
            messages.info(request, 'passwords are different')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.info(request, 'username taken')
            return redirect('register')
           
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email taken')
            return redirect('register')
         
        user = User.objects.create_user(
            username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        Client.objects.create(
            user=user, contact=contact, gender=gender, userType=userType)
        auth.login(request, user)

        return redirect('seekerDashboard')

    else:
        return render(request, 'register.html')






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



def logout(request):
    return render(request, 'recruiter.html')
    auth.logout(request)
    return redirect('home')



def landingpage(request):
    return render(request, 'landingpage.html')



def seekerDashboard(request):
    jobs = Job.objects.all()
    return render(request, 'seekerDashboard.html', {'jobs': jobs})
        


# Add job through forms.py
def jobhome(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobhome.html', {'jobs': jobs})



def profile(request):
    # user = user.objects.filter(user=request.user)
    
    # return render(request, 'profile.html', {'user': user})

    userdata = Client.objects.filter(user=request.user)
    return render(request, 'profile.html', {'userdata': userdata})



def job_details(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'job_details.html', {'jobs': jobs})


    
def savedJobs(request):
    jobs=SavedJobs.objects.filter(user=request.user)
    return render(request, 'savedjobs.html',{'jobs':jobs})



def appliedJobs(request):
    jobs=AppliedJobs.objects.filter(user=request.user)
    return render(request, 'appliedjobs.html',{'jobs':jobs})



def applicants(request):
    jobs=Job.objects.filter(user=request.user)
    return render(request, 'applicants.html',{'jobs':jobs})



def applicant(request, job_id):
    jobs=AppliedJobs.objects.filter(job=job_id, job__user=request.user)
    if(jobs):
        job=jobs[0]
    else:
        job='sorry! nobody is interested in your fucking job'
    return render(request, 'applicant.html',{'jobs':jobs,'job':job})



def list_job(request):
    form = JobForm()
    user=User.objects.get(username=request.user)
    form.fields['user'].initial  = user.id
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.fields['user'] = user
            form.save()
        return redirect('jobhome')
    return render(request, 'list_job.html', {'form': form})



def delete_job(request,id):
    obj = Job.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job deleted')
    return redirect('jobhome')



def remove_job(request,id):
    obj = SavedJobs.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job removed')
    return redirect('seekerDashboard')



def remove_applied_job(request,id):
    obj = AppliedJobs.objects.get(job_id= id)
    obj.delete()
    messages.info(request, 'job removed')
    return redirect('seekerDashboard')



def save_job(request,job_id):
    if SavedJobs.objects.filter(job_id=job_id).exists():
            messages.info(request, 'you already saved this job')
            return redirect('seekerDashboard')
    else:
        if request.user.is_authenticated:
            try:
                job=Job.objects.get(job_id=job_id)
                user=User.objects.get(username=request.user)
                saved_Jobs=SavedJobs(job=job,user=user)
                saved_Jobs.save()
                return redirect('saved_jobs')
            except:
                return redirect('saved_jobs')



def apply_job(request,job_id):
    if AppliedJobs.objects.filter(job_id=job_id).exists():
            messages.info(request, 'you already applied for this job')
            return redirect('seekerDashboard')
    else:
        if request.user.is_authenticated:
            try:
                job=Job.objects.get(job_id=job_id)
                user=User.objects.get(username=request.user)
                applied_jobs=AppliedJobs(job=job,user=user)
                applied_jobs.save()
                return redirect('appliedJobs')
            except:
                return redirect('appliedJobs')

def search(request):
    
    query = request.GET['query']
    jobs = Job.objects.filter(job_title__icontains=query)
    allJob =  {'jobs': jobs}
    return render(request, 'search.html',allJob)


def recruiter(request):
    if request.method == 'POST':
        userTypes = 'recruiter'
        CompanyEmail = request.POST['company_email']
        CompanyName = request.POST['company_name']
        Location = request.POST['location']
        CompanyType = request.POST['types']
        contactNumber = request.POST['company_number']
        personalName = request.POST['personal_name']
        personalContact = request.POST['contact']
        personalEmail = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        if password1 != password2:
            messages.info(request, 'passwords are different')
            return redirect('recruiter')

        if User.objects.filter(username=personalEmail).exists():
            messages.info(request, 'username taken')
            return redirect('recruiter')
           
        if User.objects.filter(email=CompanyEmail).exists():
            messages.info(request, 'email taken')
            return redirect('recruiter')
         
        user = User.objects.create(
            username=personalEmail, password=password1, email=CompanyEmail, first_name=CompanyName, last_name=contactNumber)
        recruiterDetails.objects.create(
            user = user,userTypes = userTypes,Location= Location,CompanyType=CompanyType,personalName=personalName,personalContact=personalContact)
        auth.login(request, user)

        return redirect('/recruiter')

    else:
        return render(request, 'recruiter.html')