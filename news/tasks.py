# import string
# from email.message import EmailMessage
# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
# from django.core.mail import EmailMessage
#
# from django.template.loader import render_to_string
# from news.models import News, NewsLetter
#
#
# @periodic_task(run_every=crontab(minute='*/1'))
# def send_mail_periodically():
#     print("hi")
#     obj = News.objects.filter(published=True,subscription=False)
#     if obj:
#         obj.update(subscription=True)
#         # obj = News.objects.last()
#         html_content = render_to_string('newsletter.html', {'news': obj})
#         print(html_content)
#         message = EmailMessage(subject='Newsletter', body=html_content,
#                                        to=list(NewsLetter.objects.filter(status=True).distinct()))
#         message.content_subtype = 'html'
#         # message.send()
#         print("hi2")
#


# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
# from django.core.mail import EmailMessage
#
#
# @periodic_task(run_every=crontab(minute='*/1'))
# def send_mail_periodically():
#     print("ITs here")
#     email = EmailMessage()
#     email.subject = "Maze mail"
#     email.body = "hello you are recieving"
#     email.to = ['atley.sayone@gmail.com',]
#     email.send()