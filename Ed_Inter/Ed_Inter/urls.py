"""
URL configuration for EdInteract project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Ed_Core import views


urlpatterns = [

   path('admin/',admin.site.urls , name='admin') ,
   path('',views.index,name="index"),
   path('index',views.index,name="index"),

   path('Login',views.Login,name="Login"),
   path('RegisterAs',views.RegisterAs,name="RegisterAs"),
   path('Student_Register',views.Student_Register,name="Student_Register"),
   path('Staff_Register',views.Staff_Register,name="Staff_Register"),
   path('st_register_submission',views.st_register_submission,name="st_register_submission"),
   path('sf_register_submission',views.sf_register_submission,name="sf_register_submission"), 
   path('Login_Submmission',views.Login_Submmission,name="Login_Submmission"),
   path('Login_Failed',views.Login_Failed,name="Login_Failed"),
   path('After_Registration',views.After_Registration,name="After_Registration"),

   path('question_post',views.question_post,name="question_post"),

   path('Profile_Update',views.Profile_Update,name="Profile_Update"),


   path('command_post/<str:answer_id>/',views.command_post,name="command_post"),
   path('command_save',views.command_save,name="command_save"), 

   path('answer_post/<int:question_id>/',views.answer_post,name="answer_post"),
   path('answer_save',views.answer_save,name="answer_save"), 

   path('reply_post/<str:commmand_id>/',views.reply_post,name="reply_post"), 
   path('reply_save',views.reply_save,name="reply_save"), 

   #path('register_submission',views.register_submission,name="register_submission"), 
   path('About',views.About,name="About"),
   path('Contact',views.Contact,name="Contact"),

   path('BacktoHome',views.BacktoHome,name="BacktoHome"),
   path('Sf_Profile_Update',views.Sf_Profile_Update,name="Sf_Profile_Update"),
   path('St_Profile_Update',views.St_Profile_Update,name="St_Profile_Update"),


  
   path('Dashboard',views.Dashboard,name="Dashboard"),
   path('Profile',views.Profile,name="Profile"),
   path('Saved_Items_List',views.Saved_Items_List,name="Saved_Items_List"),
   path('Already_Saved',views.Already_Saved,name="Already_Saved"),
   path('Save_Item/<int:question_id>/',views.Save_Item,name="Save_Item"),

]
