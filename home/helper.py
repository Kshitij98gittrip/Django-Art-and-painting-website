from django.utils.text import slugify
import string
import random

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
