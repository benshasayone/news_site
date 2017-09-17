# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect, get_list_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import ListView, DetailView, TemplateView, FormView

from news.forms import NewsletterForm, contactusForm
from news.models import News, NewsTypes, NewsLetter, Contactus
from news.tokens import account_activation_token


class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    paginate_by = 4
    context_object_name = 'news'
    queryset = News.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['news_cat_list'] = NewsTypes.objects.all()
        return context

    def get_absolute_url(self):
        return reverse('news-detail', args=[str(self.id)])


class NewsDetailView(DetailView):
    """
    To display News in detail
    """
    model = News
    template_name = 'news_details.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        get_slug = self.kwargs['slug']
        cat = self.kwargs['newstype']
        context['news_cat_list'] = NewsTypes.objects.all()
        context['news_det'] = News.objects.get(slug=get_slug)
        context['type2'] = cat
        return context


class NewsCatView(ListView):
    """
        To display News in category
    """
    model = News
    template_name = 'news_cat.html'
    paginate_by = 2
    context_object_name = 'news'

    def get_queryset(self, **kwargs):
        ntype = self.kwargs['newstype']
        get_list_or_404(News.objects.filter(news_type__type=ntype).order_by('-pub_date'), news_type__type=ntype)
        return News.objects.filter(news_type__type=ntype).order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(NewsCatView, self).get_context_data(**kwargs)
        ntype = self.kwargs['newstype']
        context['news_cat_list'] = NewsTypes.objects.all()
        context['type1'] = ntype
        return context


class NewsSearchView(ListView):
    model = News
    template_name = 'results.html'
    context_object_name = 'results'

    def get_queryset(self, **kwargs):
        if self.request.is_ajax():
            q = self.request.GET.get('q')
            if q is not None:
                return News.objects.filter(
                    Q(title__icontains=q)).order_by('-pub_date')


class NewsSearchCatView(ListView):
    model = News
    template_name = 'results.html'
    context_object_name = 'results'

    def get_queryset(self, **kwargs):
        if self.request.is_ajax():
            q = self.request.GET.get('q')
            w = self.request.GET.get('w')
            if q is not None:
                return News.objects.filter(news_type__type=w).filter(
                    Q(title__icontains=q)).order_by('-pub_date')


@receiver(post_save, sender=News)
def send_user_data_when_created_by_admin(sender, instance, **kwargs):
    obj = News.objects.last()
    html_content = render_to_string('newsletter.html', {'news': obj})
    message = EmailMessage(subject='Newsletter', body=html_content,
                           to=list(NewsLetter.objects.filter(status=True).distinct()))
    message.content_subtype = 'html'
    message.send()


class SubscribeView(FormView):
    form_class = NewsletterForm
    success_url = 'newsletterregister.html'

    def form_valid(self, form):
        obj = NewsLetter.objects.filter(email=form.cleaned_data['email'])
        if obj:
            if NewsLetter.objects.filter(email= form.cleaned_data['email'],status =True).exists():
                obj = NewsLetter.objects.get(email=form.cleaned_data['email'], status=True)
                mail_subject = 'Activate your NewsLetter Subscription'
                message = render_to_string('alreadyactive.html',{
                    'user': obj.email,
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
            else:
                obj = NewsLetter.objects.get(email=form.cleaned_data['email'])
                current_site = get_current_site(self.request)
                mail_subject = 'Activate your NewsLetter Subscription'
                message = render_to_string('acc_active_email.html', {
                    'user': obj.email,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
                    'token': account_activation_token.make_token(obj),
                })
                obj.token = account_activation_token.make_token(obj)
                obj.save()
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
        else:
            obj = NewsLetter.objects.create(email=form.cleaned_data['email'], token='123456789', status=False)
            obj.save()
            current_site = get_current_site(self.request)
            mail_subject = 'Activate your NewsLetter Subscription'
            message = render_to_string('acc_active_email.html', {
                'user': obj.email,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(obj.pk)),
                'token': account_activation_token.make_token(obj),
            })
            obj.token = account_activation_token.make_token(obj)
            obj.save()
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
        return redirect('news:news-list')


class ActivateView(TemplateView):
    template_name = 'activate.html'

    def get_context_data(self, **kwargs):
        context = super(ActivateView, self).get_context_data(**kwargs)
        uidb64 = self.kwargs['uidb64']
        token = self.kwargs['token']
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            obj = NewsLetter.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, obj.DoesNotExist):
            obj = None
        if obj is not None and account_activation_token.check_token(obj, token):
            obj.status = True
            obj.save()
            context['message'] = 'Thank you for your email confirmation. Now you will our Newsletter every time a news is added'

        else:
            context['message'] = 'Activation link is invalid!'
        return context


class ContactusView(FormView):
    template_name = 'contact_page.html'
    form_class = contactusForm
    success_url = 'contactusconfirm.html'

    def form_valid(self, form):
        obj = Contactus.objects.create(name=form.cleaned_data['name'],
                                       email=form.cleaned_data['email'], subject=form.cleaned_data['subject'],
                                       message=form.cleaned_data['data'])
        obj.save()
        mail_subject = 'NewsCorner - Contact us - Page'
        mail_subject2 = 'NewsCorner - Contact Us ' + obj.subject
        message = render_to_string('contactus_email.html', {
            'user': obj.email,
        })
        message2 = render_to_string('contactus_email2.html', {
            'user': obj.name,
            'email': obj.email,
            'subject': obj.subject,
            'message': obj.message,

        })
        to_email = obj.email
        obj = User.objects.get(is_superuser=True)
        to_email2 = obj.email
        email2 = EmailMessage(
            mail_subject2, message2, to=[to_email2]
        )
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        email2.send()
        return super(ContactusView, self).form_valid(form)


class my_custom_page_not_found_view(TemplateView):
    template_name = '404_page.html'
