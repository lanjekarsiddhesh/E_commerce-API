from django.core.mail import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()

class Util:
    @staticmethod
    def send_mail(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            from_email=os.getenv('EMAIL_HOST_USER'),
            to=[data['to']]
        )
        email.send()