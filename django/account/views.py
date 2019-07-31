from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import LoginForm


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


@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                  {'section': 'dashboard'})
