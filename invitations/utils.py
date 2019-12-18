from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

def send_email(email):
    subject = 'Invitation!'
    from_email= settings.EMAIL_HOST_USER
    text_content = "You got New Invitation!"
    mail = EmailMultiAlternatives(subject, text_content, from_email, [email])
    mail.send()
    return Response({"message" : "Mail with Invitation has been sent successfully"}, status=status.HTTP_200_OK) 
