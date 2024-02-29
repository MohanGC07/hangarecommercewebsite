from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db import transaction
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User

from .forms import  UserRegisterForm,EditProfileForm
from django.urls import resolve
from authy.models import Profile
# Create your views here.
@login_required
def UserProfile(request, username):
    user = get_object_or_404(User, username=username)
    profile, created = Profile.objects.get_or_create(user=user)

  
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


@login_required
def EditProfile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile.image = form.cleaned_data.get('image')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.bio = form.cleaned_data.get('bio')
            profile.save()
            return render(request,'index.html')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'editprofile.html', context)





def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Automatically Log In The User
            login(request, new_user)

            return redirect('ShopHome')
    else:
        if request.user.is_authenticated:
            return redirect('ShopHome')
        else:
            form = UserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'sign-up.html', context)


def logout_view(request):
    logout(request)
    return redirect('sign-in')  # Redirect to the homepage or any other page

# In your login view, redirect to index.html upon successful login
@login_required
def login(request):
    return redirect('ShopHome')

