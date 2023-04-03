from django.db import models
from .helper import *
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser
# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=120)
    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    citys=models.CharField(max_length=30)
    state=models.CharField(max_length=10)
    desc=models.TextField()
    # photo=models.ImageField(upload_to="user_images")
    date=models.DateField()

    def __str__(self):
        return self.name
class Image(models.Model):
    email=models.CharField(max_length=120)
    name=models.CharField(max_length=120)
    phone=models.CharField(max_length=120)
    citys=models.CharField(max_length=30)
    state=models.CharField(max_length=10)
    desc=models.TextField()
    photo=models.ImageField(upload_to="user_images")
    date=models.DateTimeField(auto_now_add=True)
class Upl_image(models.Model):
    id=models.AutoField(primary_key=True)
    # email=models.CharField(max_length=120)
    name=models.CharField(max_length=120)
    title=models.CharField(max_length=200)
    # citys=models.CharField(max_length=30)
    # state=models.CharField(max_length=10)
    artype=models.CharField(max_length=400)
    aboutyou=models.TextField()
    aboutart=models.TextField()
    insta=models.CharField(max_length=2000)
    fb=models.CharField(max_length=2000)
    otherlink=models.CharField(max_length=2000)
    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE)
    # insta=models.CharField(max_length=300)
    # fb=models.CharField(max_length=300)
    # desc=models.TextField()
    photo=models.ImageField(upload_to="user_images")
    date=models.DateTimeField(auto_now_add=True)
    slug=models.CharField(max_length=130)
    def __str__(self):
        return self.name
    
    def save(self,*args, **kwargs):
        self.slug=generate_slug(self.name)
        super(Upl_image,self).save(*args, **kwargs)

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    token=models.CharField(max_length=100)
    is_verifed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

     