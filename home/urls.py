from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index,name="home"),
    path('aboutus',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('register',views.registeruser,name="registeruser"),
    path('login',views.loginuser,name="loginuser"),
    path('logout',views.logoutuser,name="logoutuser"),
    path('blog',views.blog,name="blog"),
    path('blogpost/<slug>',views.blogpost,name="blogpost"),
    # path('delete/<int:id>',views.deleteblog,name="deleteblog"),
    path('blogpost/delete/<int:id>', views.delete, name="delete"),
    path('myblog', views.myblog, name="myblog"),
]