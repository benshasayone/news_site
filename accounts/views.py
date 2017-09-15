from allauth.account.views import SignupView, LoginView, PasswordResetView, EmailVerificationSentView, ConfirmEmailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.checks import messages
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from accounts.forms.forms import SignUpForm
from accounts.templates.forms import editform


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

@login_required
def editprofile(request,):
    if request.method == 'POST':
        form = editform(request.POST)
        if form.is_valid():
            user = User.objects.get_by_natural_key(username=form.cleaned_data['username'])
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('account_edit')
    else:
        form = editform()
    return render(request, 'profile_edit.html')

class MySignupView(SignupView):
    template_name = 'signup2.html'


class MyLoginView(LoginView):
    template_name = 'login2.html'

# class MyPasswordResetView(PasswordResetView):
#     template_name = 'login2.html'


class MyEmailVerificationSentView(EmailVerificationSentView):
    template_name = 'Emailverficationsent.html'


class MyConfirmEmailView(ConfirmEmailView):
    template_name = 'ConfirmEmail.html'