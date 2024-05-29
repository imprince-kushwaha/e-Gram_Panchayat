from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from datetime import datetime


class Aadhar(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    aadhar=models.BigIntegerField()

    # def clean(self):
    #     cleaned_data=super().clean()
    #     name=cleaned_data.get('name')

    #     if name and len(name)<9:
    #         self.add_error('name','name should be atleast 9 characters long')


class Birth(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    DOB=models.DateField()
    name=models.CharField(max_length=30)
    gen=models.CharField(max_length=30)
    f_name=models.CharField(max_length=30)
    m_name=models.CharField(max_length=30)
    dis_name=models.CharField(max_length=30)
    place_of_bir=models.CharField(max_length=30)
    bp_address=models.CharField(max_length=30)
    c_address=models.CharField(max_length=30)
    p_address=models.CharField(max_length=30)
    email=models.EmailField()
    num=models.IntegerField()
    m_edu=models.CharField(max_length=30)
    m_occ=models.CharField(max_length=30)
    f_edu=models.CharField(max_length=30)
    f_occ=models.CharField(max_length=30)
    m_age_mar=models.IntegerField()
    m_age_del=models.IntegerField()
    date=models.DateField()
    appli_name=models.CharField(max_length=30)

class Death(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    applicant_name=models.CharField(max_length=30)
    applicant_relation=models.CharField(max_length=30)
    mobile=models.IntegerField()
    date_of_death=models.DateField()
    deceased_name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    deceased_fname=models.CharField(max_length=30)
    deceased_mname=models.CharField(max_length=30)
    religion=models.CharField(max_length=30)
    death_age=models.IntegerField()
    cause_of_death=models.CharField(max_length=100)
    deceased_address=models.CharField(max_length=50)
    date_of_issue=models.DateTimeField(default=datetime.now())
    
class Complaint(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    compl_type=models.CharField(max_length=30)
    compl_loc=models.CharField(max_length=300)
    date_time=models.DateTimeField(default=datetime.now())
    desc=models.CharField(max_length=300)
    document=models.ImageField(default="")
    status=models.CharField(max_length=30,choices=[("Incomplete","Incomplete"),("Pending","Pending"),("Complete","Complete")],default="Incomplete")

class Contacts(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    c_name=models.CharField(max_length=30)
    c_mail=models.EmailField()
    c_mssg=models.CharField(max_length=200)


