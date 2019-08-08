from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import (LoginForm, UserRegistrationForm,
                    UserEditForm, ProfileEditForm)
from .models import Profile


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user_name = data['username']
            user_pass = data['password']
            # Try to authenticate the user
            user = authenticate(request, username=user_name,
                                password=user_pass)
            if user is not None:
                if user.is_active:
                    return HttpResponse('User authenticated\
                         successfully')
                else:
                    # Then the user is deactivate
                    return HttpResponse('Your account is disabled')
            else:
                # Can't log the user
                return HttpResponse('Invalid credentials provided !')
    else:
        # It's a get request, then show the login form
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Create the user profile
            Profile.objects.create(user=new_user)
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'account/register.html',
                  {'user_form': user_form})


@login_required
def edit(request):
    SUCCESS_MESSAGE = "Profile updated successfully !"
    ERROR_MESSAGE = "Error while updating your profile !"
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, SUCCESS_MESSAGE)
        else:
            messages.error(request, ERROR_MESSAGE)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html',
                  {'user_form': user_form, 'profile_form': profile_form})
