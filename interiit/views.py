from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from interiit.models import Profile, Details
from interiit.forms import ProfileRegistrationForm
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms.formsets import formset_factory
from django.contrib.auth import logout
from django.template import loader, RequestContext
from django.conf import settings
from django.core.files.base import ContentFile

import os

@login_required
def main_page(request):
    detail = Details.objects.get(user=request.user)
    sport = detail.sport
    user = request.user
    return render(request, 'portal_page.html',{'user' : user, 'sport' : sport}) 

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login/') 

@login_required
def profile_register(request):
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.pk
            post.save()
            return HttpResponseRedirect('/profile/list')
    
    else:
        form = ProfileRegistrationForm()
    details = Details.objects.get(user=request.user)

    return render(request, 'register.html', {'form' : form , 'sport' : str(details.sport)})

@login_required
def profile_edit(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id)
    except Exception, e:
        return render(request, 'profileEdit.html', {'error' : 'yes','message': "This ID does not exist" })
    if profile.user == request.user :
        pass
    else :
        return render(request, 'profileEdit.html', {'error' : 'yes','message': "You do not have access to this ID" })
    if request.method == 'POST':
        form = ProfileRegistrationForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user.pk
            post.save(force_update=True)
            return HttpResponseRedirect('/profile/list/')   
    else:
        form = ProfileRegistrationForm(instance=profile)
    details = Details.objects.get(user=request.user)
    return render(request, 'profileEdit.html', {'form' : form , 'profile_id' : profile_id, 'error' : 'no',  'sport' : str(details.sport)  })

@login_required
def profile_delete(request, profile_id):
    try:
        Profile.objects.get(pk=profile_id).delete()
        profiles = Profile.objects.filter(user=request.user)
    except Exception, e:
        return render(request, 'profileEdit.html', {'error' : 'yes','message': "This ID does not exist" })
    
    return HttpResponseRedirect('/profile/list')

@login_required
def profile_list(request):
    user = request.user
    profiles = Profile.objects.filter(user_id=user.pk)
    details = Details.objects.get(user=request.user)
    return render(request, 'profileList.html', { 'profiles_list' : profiles, 'sport':details.sport })