from allauth.account.signals import user_signed_up
from django.dispatch import receiver


@receiver(user_signed_up)
def user_signed_up_(request, user, sociallogin=None, **kwargs):
    if sociallogin:
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'Facebook':
            user.first_name = sociallogin.account.extra_data['first_name']
            user.last_name = sociallogin.account.extra_data['last_name']
            user.email = sociallogin.account.extra_data['email']


        if sociallogin.account.provider == 'Google':
            user.first_name = sociallogin.account.extra_data['given_name']
            user.last_name = sociallogin.account.extra_data['family_name']
            user.email = sociallogin.account.extra_data['email']


        user.save()

