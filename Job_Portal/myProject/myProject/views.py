from django.shortcuts import render,redirect

from myApp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def signupPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("Confirm_password")
        user_type=request.POST.get("user_type")
        image=request.FILES.get("image")
    
        
        if password==Confirm_password:
            
            
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=image,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("signInPage")
            
    return render(request,"signupPage.html")


def signInPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('signInPage')

    return render(request, 'signInPage.html')

@login_required
def homePage(request):
    
    totaljob=JobModel.objects.all().count()
    totaluser=customUser.objects.all().count()
    total_apply=jobApplyModel.objects.all().count()
    latest_jobs = JobModel.objects.order_by('-created_at')[:3]
    
    context={
        'totaljob':totaljob,
        'totaluser':totaluser,
        'total_apply':total_apply,
        'latest_jobs':latest_jobs,
    }
    
    return render(request,"homePage.html",context)


def logoutPage(request):
    
    logout(request)
    
    return redirect('signInPage')

@login_required
def profilePage(request):
    
    return render(request,"profilePage.html")

def addJob(request):


    if request.method == 'POST':
        Job_title = request.POST.get('title')
        vacancy = request.POST.get('vacancy')
        description = request.POST.get('description')
        category = request.POST.get('category')
        skills = request.POST.get('skills')
        job_image = request.FILES.get('Job_Image')
        

        job = JobModel(
            user=request.user,
            job_title=Job_title,
            category=category,
            vacancy=vacancy,
            job_description=description,
            image=job_image,
            skills=skills,
        )
        job.save()
        return redirect("createdJob")

        
     
    return render(request, 'addJob.html')

def createdJob(request):

    current_user=request.user
    job=JobModel.objects.filter(user=current_user)

    context={
        'job':job
    }
    
    return render(request,"createdJob.html",context)


def jobFeed(request):
    job=JobModel.objects.all()
    context={
        'job':job
    }
    return render(request,"jobFeed.html",context)


def deleteJob(request,id):

    
    job=JobModel.objects.get(id=id).delete()
    return redirect("createdJob")




def viewJob(request,id):
    job=JobModel.objects.get(id=id)

    context={
        'job':job
    }
    return render(request,"viewJob.html",context)


def applyJob(request,id):
    job=JobModel.objects.get(id=id)

    context={
        'job':job
    }
    
    if request.method=='POST':
            Skills=request.POST.get('skills')
            Cover=request.FILES.get('cover')
            Resume=request.FILES.get('resume')
            applyImage=request.POST.get('applyImage')
            apply=jobApplyModel(
                user=request.user,
                job=job,
                Skills=Skills,
                Resume=Resume,
                Cover=Cover,
                apply_image=applyImage,  
            )
            apply.save()
            return redirect("jobFeed")

    return render(request,"applyJob.html",context)





def editJob(request,id):


    job=JobModel.objects.get(id=id)


    if request.method == 'POST':
        Id=request.POST.get('id')
        Job_title = request.POST.get('title')
        vacancy = request.POST.get('vacancy')
        description = request.POST.get('description')
        category = request.POST.get('category')
        skills = request.POST.get('skills')
        job_image = request.FILES.get('Job_Image')
        

        job = JobModel(
            id=Id,
            user=request.user,
            job_title=Job_title,
            category=category,
            vacancy=vacancy,
            job_description=description,
            image=job_image,
            skills=skills,
        )
        job.save()
        return redirect("createdJob")
    else:
        
        messages.warning(request,"You are not Recruiter")

    context={
        'job':job
    }
    
    return render(request,"editJob.html",context)

def searchJob(request):
    
    query = request.GET.get('query')
    
    job = JobModel.objects.filter(Q(job_title__icontains=query) 
                                       |Q(category__icontains=query)  
                                       |Q(skills__icontains=query))
     
    context={
        'query':query,
        'job':job
    }
    
    return render(request,"searchJob.html",context)



def skillMatching(request):
    user=request.user
    
    mySkill=user.skills
    
    
    job=JobModel.objects.filter(skills=mySkill)
    
    context={
        'job':job
    }
    
    
    return render(request,"skillMatching.html",context)



