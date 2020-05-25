from django.shortcuts import render,redirect
from .forms import*
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from quest.models import Post
from .models import Profile
import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Successfuly Created Account! Please log in.')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    username=request.user
    context={'posts':Post.objects.filter(author=username).order_by('-date_posted')}
    return render(request,'users/profile.html',context=context)

@login_required
def UpdateSettings(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        #request.FILES is for image data

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile Updated Succesfully!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={'u_form':u_form,'p_form':p_form}


    return render(request,'users/updateSettings.html',context=context)



