from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from common.decorators import ajax_required
from actions.utils import create_action

from .forms import (LoginForm, UserRegistrationForm,
                    UserEditForm, ProfileEditForm)
from .models import Profile, Contact


@login_required
def dashboard(request):
    # Display alls actions by default apart for the
    # current user
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id', flat=True)

    # If user is following others, retrieve only their actions
    if following_ids:
        actions = actions.filter(user_id__in=following_ids)
    # Take only the first 10 of the list
    actions = actions[:10]
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard', 'actions': actions})


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
            # Create an action
            create_action(new_user, 'has created an account')
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


@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
                  'account/user/list.html',
                  {'section': 'people',
                   'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
                             username=username,
                             is_active=True)
    return render(request,
                  'account/user/detail.html',
                  {'section': 'people', 'user': user}
                  )


@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user)
                # Create a action
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            # Error when try to retrieve the user
            return JsonResponse({'status': 'ko'})
    # Some data(user_id or action) is not present
    return JsonResponse({'status': 'ko'})
