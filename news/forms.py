from django import forms


class NewsletterForm(forms.Form):
    email = forms.EmailField(help_text='Required')


class contactusForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    data = forms.CharField()
