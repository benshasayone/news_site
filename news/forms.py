from django import forms

from news.models import NewsLetter


class NewsletterForm(forms.Form):
    email = forms.EmailField(help_text='Required')
