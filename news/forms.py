from django import forms



class NewsletterForm(forms.Form):
    email = forms.EmailField(help_text='Required')
