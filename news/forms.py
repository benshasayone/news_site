from django import forms

from news.models import Contactus


class NewsletterForm(forms.Form):
    email = forms.EmailField(help_text='Required')


class ContactusForm(forms.ModelForm):

    class Meta:
        model = Contactus
        fields = ('name', 'email','subject', 'message')