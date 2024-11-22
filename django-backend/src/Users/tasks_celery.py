from celery import shared_task
from django.core.mail import send_mail
from online_streaming.settings import EMAIL_HOST_USER
def sending_email(link, email_user):
    send_mail(
        subject='Подтверждение регистрации',
        message=f'Перейдите по ссылке {link}',
        from_email= EMAIL_HOST_USER,
        recipient_list= [email_user],
        fail_silently=False,
        )