from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime 
from home.models import Upl_image,Profile
from django.contrib.auth import authenticate
from django.contrib.auth import logout,login
import re
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .helper import *
# Create your views here.
def index(request):
    # allPost=Upl_image.objects.all()
    # # print(allPosts)
    # context={'allPost': allPost}
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.user.is_anonymous:
        return redirect("/register")
    if request.method=="POST":
        name=request.POST.get('name')
        title=request.POST.get('title')
        artype=request.POST.get('artype')
        aboutyou=request.POST.get('aboutyou')
        aboutart=request.POST.get('aboutart')
        insta=request.POST.get('insta')
        fb=request.POST.get('fb')
        user=request.user
        print(user)
        otherlink=request.POST.get('otherlink')
        if len(request.FILES)!=0:
            photo=request.FILES['image_u']
        # if Upl_image.objects.filter(email=email).exists():
        #     messages.warning(request, "Email Is Already Taken!",extra_tags='mail_exist')
        #     return redirect('/contact')
        upl_img=Upl_image(name=name,title=title,artype=artype,aboutyou=aboutyou,aboutart=aboutart,insta=insta,fb=fb,otherlink=otherlink,user=user,photo=photo,date=datetime.today())
        upl_img.save()
        messages.success(request, 'Information saved successfully!',extra_tags='contact_tag')

    return render(request,'contact.html')
def registeruser(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        email=request.POST.get('email')
        # gender=request.POST.get('gender')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        try:
            if User.objects.filter(username = username).exists():
                messages.warning(request, "Username Is Already Taken",extra_tags='username_exist')
                return redirect('/register')
            elif User.objects.filter(email = email).exists():
                messages.warning(request, 'EMAIL Already Exists.',extra_tags='email_exist')
                return redirect('/register')
            
            # pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"

        
            if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', pass1):
                # print(special_char.search(pass1))
                messages.warning(request,"Password does not contain special character!",extra_tags='spec_char')
                return redirect('/register')
            elif len(pass1)<8:
                messages.warning(request,"Password is very short!",extra_tags='pass_len')
                return redirect('/register')
            elif pass1!=pass2:
                messages.warning(request,"Password and confirm password don't match!",extra_tags='val_pass')
                return redirect('/register')
            my_user=User.objects.create_user(username=username,email=email,password=pass1)
            my_user.first_name=firstname
            my_user.last_name=lastname
            my_user.save()
            messages.success(request, 'Registration is successful. Now you can login!',extra_tags='sucess_exist')
            token=genRandomString(20)
            Profile.objects.create(user=my_user,token=token)
            send_mail_to_user(token,email)
            # auth_token=str(uuid.uuid4())
            # profile_obj=Profile.objects.create_user(user=my_user,auth_token=auth_token)
            # profile_obj.save()
            # send_mail_after_register(email,auth_token)
            # return redirect('/token')
        except Exception as e:
            print(e)
        
        # return HttpResponse("Registration is successful!")
        # print(username,email,gender,pass1,pass2)
         
    return render(request,'register.html')
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user=User.objects.get(username=User.username).first()
        if not Profile.objects.filter(user=check_user).first().is_verifed:
            messages.error(request,'Your profile is not verified',extra_tags='prof_verify')
            raise Exception('profile not verified')
        # password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/contact")
        else:
            messages.warning(request, "User is not registered",extra_tags='user_exist')
            return render(request,'login.html')
    
    return render(request,'login.html')

    # return render(request,'login.html')
def logoutuser(request):
    logout(request)
    return redirect("/login")
    # return render(request,'logout.html')
def blog(request):
    allPosts=Upl_image.objects.all()
    # print(allPosts)
    context={'allPosts': allPosts}
    return render(request,'blog.html',context)
def blogpost(request,slug):
    allBlogs=Upl_image.objects.filter(slug=slug).first()
    # print(allPosts)
    context1={'post': allBlogs}
    return render(request,'blogpost.html',context1)
def delete(request,id):
    post_to_delete=Upl_image.objects.get(id=id)
    post_to_delete.delete()
    return redirect("/blog")
def myblog(request):
    context = {}

    # try:
    usr=request.user.id
    print(usr)
    blog_objs = Upl_image.objects.filter(user=usr)
    print(blog_objs)
    context['blog_objs'] = blog_objs
    # except Exception as e:
    #     print(e)

    print(context)
    # # return render(request, 'see_blog.html', context)
    
    
    return render(request,'my_blog.html',context)

def verify(request,token):
    try:
        profile_obj=Profile.objects.filter(token=token).first()

        if profile_obj:
            profile_obj.is_verifed=True
            profile_obj.save()
        return redirect('/login')
    except Exception as e:
        print(e)
    return redirect('/')