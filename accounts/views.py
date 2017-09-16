from allauth.account.views import SignupView, LoginView, EmailVerificationSentView, ConfirmEmailView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.templates.forms import editform


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
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'login.html'

# class MyPasswordResetView(PasswordResetView):
#     template_name = 'login2.html'


class MyEmailVerificationSentView(EmailVerificationSentView):
    template_name = 'Emailverficationsent.html'


class MyConfirmEmailView(ConfirmEmailView):
    template_name = 'ConfirmEmail.html'