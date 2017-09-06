from allauth.account.signals import user_logged_in
from allauth.account.views import SignupView
from allauth.socialaccount.helpers import _add_social_account
from allauth.socialaccount.models import SocialLogin
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.checks import messages
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('news:news-list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
