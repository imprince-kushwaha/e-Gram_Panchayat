from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('home/',views.Home,name='home'),
    path('signup/',views.Signup,name='signup'),
    path('signin/',views.Signin,name='signin'),
    path('menu/',views.Menu,name='menu'),
    path('logout/',views.Logout,name='logout'),
    path('aadhar/',views.Aadhar_val,name='aadhar'),
    path('contact/',views.Contact,name='contact'),
    path('about/',views.About,name='about'),
    path('birth_form/',views.Birth_reg,name='birth_form'),
    path('death_form/',views.Death_reg,name='death_form'),
    path('death_cert/',views.Death_cert,name='death_cert'),
    path('birth_cert/',views.Birth_cert,name='birth_cert'),
    path('my_cert/',views.Showcertificate,name='my_cert'),
    path('complaint/',views.Complaint_reg,name='complaint'),
    path('my_complaint/',views.Mycomplaint,name='my_complaint'),

]