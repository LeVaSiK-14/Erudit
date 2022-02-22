from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_gmail(name, last_name, email, phone_number, text):
    send_mail(subject=f'{last_name} {name}',
              message=f'{text}\n\n{phone_number}',
              recipient_list=[email, ],
              from_email=None)