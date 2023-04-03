from django.utils.text import slugify
import string
import random
from django.conf import settings
from django.core.mail import send_mail
def genRandomString(N):
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits,k=N))
    return str(res)
def generate_slug(txt):
    newslug=slugify(txt)
    from .models import Upl_image
    if Upl_image.objects.filter(slug=newslug).exists():
        
        return generate_slug(txt+genRandomString(5))
    return newslug

def send_mail_to_user(token,email):
    subject="Your account needs to be verified"
    message=f"Paste or click the link to verify your account http://127.0.0.1:8000/verify/{token}"
    email_from=settings.EMAIL_HOST_USER
    recipient_list=[email]
    send_mail(subject,message,email_from,recipient_list)
    return True

