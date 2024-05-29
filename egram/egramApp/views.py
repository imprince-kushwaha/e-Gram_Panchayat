from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from egramApp.models import Aadhar
from egramApp.models import Birth
from egramApp.models import Death
from egramApp.models import Complaint
from egramApp.models import Contacts
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def Aadhar_val(request):
    if request.method=='POST':
        adh=request.POST.get('aadhar')
        try:
            ad=Aadhar.objects.get(aadhar=adh)
            # response_data={'message':'found'}
            return redirect('signin')
        except Aadhar.DoesNotExist:
            # response_data={'message':'not found'}
            return HttpResponse("not matched!!! ")
        return JsonResponse(response_data)

        # list=[]
        # list1=[]
        # adh=request.POST.get('aadhar')
        # print(adh)
        # ad=Aadhar.objects.filter(aadhar=adh)
        # list1=adh
        # print(ad)
        # for i in ad:
        #     list.append(i.aadhar)
        # print(list[0])
        # print(type(list[0]))
        # if list==list1:
        #     return redirect('signin')
        # else:
        #     return HttpResponse("not matched")
        # for i in ad:
        # print(i.aadhar)
        
        # if adh==list[0]:
        #     return redirect('signin')
        # else:
        #     return HttpResponse("not matched!!! ")
    return render(request,'aadhar.html')


def Home(request):
    return render(request,'home.html')

@login_required(login_url='signin')
def Menu(request):
    return render(request,'menu.html')

def Signup(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        # if pass1!=pass2:
        #     return HttpResponse("Your Password and Confirm password is not same")
        # else:
        #     my_user=User.objects.create_user(uname,email,pass1)
        #     my_user.save()
        #     return redirect('signin')

        error=None
        if pass1!=pass2:
            return HttpResponse("Your Password and Confirm password is not same")
        elif(len(pass1)<8 or not any(char.isdigit() for char in pass1) or not any(char.isupper() for char in pass1)or not any(char.islower() for char in pass1)
        or not any(char in '!@#$%^&*()_+' for char in pass1)):
            error="Password must contain uppercase,lowercase and special character."
            return render(request,'login.html',{'error':error})
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('signin')

            # if(
            #     len(pass1)<8
            #     or not any(char.isdigit() for char in pass1)
            #     or not any(char.isupper() for char in pass1)
            #     or not any(char.islower() for char in pass1)
            #     or not any(char in '!@#$%^&*()_+' for char in pass1)):
            #     error="Password must contain uppercase,lowercase and special character."
            #     return render(request,'login.html',{'error':error})

        




    # else:
    #     action="go_to_signin"
    #     if action=="go_to_signin":
    #         redirect('signin')

    # validation of form
        # error_message=None
        # if not pass1:
        #     error_message="Password required!!!"
        #     elif len(pass1)>8:
        #         error_message="password must be greater than 8 or more"

        #         if not error_message:
        #         my_user=User.objects.create_user(uname,email,pass1)
        #         my_user.save()
        #         else:return render(request,signup,{'error':error_message})


    return render(request,'login.html')

def Signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.success(request, 'Logged In Successfully!!')
            return redirect('menu')
        else:
            return HttpResponse("Username or Password is incorrect")
    # else:
    #     action="go_to_signup"
    #     if action=="go_to_signup":
    #         redirect('signup')
    return render(request,'login.html')


def Logout(request):
    logout(request)
    return redirect('signin')


def Contact(request):
    if request.method=='POST':
        contact_name=request.POST.get('cont_name')
        contact_email=request.POST.get('cont_email')
        contact_message=request.POST.get('cont_message')
        contact_data=Contacts(user=request.user,c_name=contact_name,c_mail=contact_email,c_mssg=contact_message)
        contact_data.save()
        return redirect('menu')
    return render(request,'contact.html')

def About(request):
    return render(request,'about.html')

def Birth_reg(request):
    if request.method=='POST':
        # username=request.POST.get('contact-username')
        dob=request.POST.get('dob')
        name=request.POST.get('name')
        gen=request.POST.get('gender')
        f_name=request.POST.get('fname')
        m_name=request.POST.get('mname')
        dis_name=request.POST.get('dname')
        pob=request.POST.get('place')
        birth_add=request.POST.get('baddress')
        curr_add=request.POST.get('caddress')
        per_add=request.POST.get('paddress')
        email=request.POST.get('email')
        mob=request.POST.get('mobile')
        mot_edu=request.POST.get('motedu')
        mot_occ=request.POST.get('motocc')
        fat_edu=request.POST.get('fatedu')
        fat_occ=request.POST.get('fatocc')
        marr_age=request.POST.get('mar_age')
        deli_age=request.POST.get('del_age')
        date=request.POST.get('date')
        applicant=request.POST.get('app_name')
        birth=Birth(user=request.user,DOB=dob,name=name,gen=gen,f_name=f_name,m_name=m_name,dis_name=dis_name,place_of_bir=pob,bp_address=birth_add
                    ,c_address=curr_add, p_address=per_add,email=email,num=mob,m_edu=mot_edu,m_occ=mot_occ,f_edu=fat_edu,
                    f_occ=fat_occ,m_age_mar=marr_age,m_age_del=deli_age,date=date,appli_name=applicant)
        # birth.save()
        # return redirect('home')
        # existing_data=Birth.objects.all()
        existing_data = Birth.objects.filter(
    DOB=dob, name=name, gen=gen, f_name=f_name, m_name=m_name, dis_name=dis_name,
    place_of_bir=pob, bp_address=birth_add, c_address=curr_add, p_address=per_add,
    email=email, num=mob, m_edu=mot_edu, m_occ=mot_occ, f_edu=fat_edu, f_occ=fat_occ,
    m_age_mar=marr_age, m_age_del=deli_age, date=date, appli_name=applicant
)       
        # error=None,success-None
        if existing_data.exists():
            # error="Data Already Exists."
                # messages.error(request,"already exists")
            messages.error(request, 'The Data Already Exists!!')
            return redirect('menu')
            
        else:
            birth.save()
            # success="Form Filled Successfully."
                # messages.success(request,"message saved")
            messages.success(request, ' Birth Form Filled Successfully!!')
            return redirect('menu')
        
    # else:
    #     return HttpResponse("something went wrong")
    return render(request,'birth_form.html')

def Death_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        relation=request.POST.get('dec_rel')
        mobile=request.POST.get('dec_mob')
        d_of_death=request.POST.get('dod')
        dname=request.POST.get('dec_name')
        gender=request.POST.get('gender')
        d_fat=request.POST.get('dec_fat')
        d_mot=request.POST.get('dec_mot')
        rel=request.POST.get('rel')
        age_death=request.POST.get('dec_death')
        cau=request.POST.get('dec_cause')
        add=request.POST.get('dec_add')
        death=Death(user=request.user,applicant_name=name,applicant_relation=relation,mobile=mobile,
                    date_of_death=d_of_death,deceased_name=dname,gender=gender,
                    deceased_fname=d_fat,deceased_mname=d_mot,religion=rel,
                    death_age=age_death,cause_of_death=cau, deceased_address=add)

        existing_data = Death.objects.filter(
            applicant_name=name, applicant_relation=relation, mobile=mobile,
            date_of_death=d_of_death, deceased_name=dname, gender=gender,
            deceased_fname=d_fat, deceased_mname=d_mot, religion=rel,
            death_age=age_death, cause_of_death=cau, deceased_address=add
        )
        if existing_data.exists():
            messages.error(request, 'The Data Already Exists!!')
            return redirect('menu')
        else:
            death.save()
            messages.success(request, ' Death Form Filled Successfully!!')
            return redirect('menu')
        # death.save()
        # messages.success(request, 'Form Filled Successfully!!')
        # return redirect('menu')
    
    return render(request,'death_form.html')

def Death_cert(request):
    if request.method=='POST':
        b=request.POST.get('view-certificate')
        death_data=Death.objects.filter(id=b)
    # for i in death_data:
    #     print(i.deceased_name)
    data={
        'death_data':death_data,
    }

    return render(request,'death_certificate.html',data)

def Birth_cert(request):
    if request.method=='POST':
        a=request.POST.get('view-certificate')
        birth_data=Birth.objects.filter(id=a)
        data={
            'birth_data':birth_data,
        }

    return render(request,'birth_certificate.html',data)

def Showcertificate(request):
    if request.user.is_staff:
        my_death=Death.objects.all()
        my_birth=Birth.objects.all()
        
    else:

        my_death=Death.objects.filter(user=request.user)
        my_birth=Birth.objects.filter(user=request.user)
        
    
    data={
        'my_death':my_death,
        'my_birth':my_birth,
    }
    return render(request,'mycertificate.html',data)

def Complaint_reg(request):
    if request.method=='POST':
        complaint_type=request.POST.get('complaint-type')
        complaint_location=request.POST.get('complaint-location')
        complaint_datetime=request.POST.get('complaint-date-time')
        complaint_description=request.POST.get('complaint-description')
        complaint_document=request.POST.get('complaint-attachment')
        complaint=Complaint(user=request.user,compl_type=complaint_type,
                            compl_loc=complaint_location,date_time=complaint_datetime,
                            desc=complaint_description,document=complaint_document)
       
        complaint.save()
        messages.success(request,  'Complain Form Filled Successfully!!')
        return redirect('menu')
    # compl_info=Complaint.objects.all()
    # data={
    #     'compl_info':compl_info,
    # }
    return render(request,'complaint.html')

def Mycomplaint(request):
    if request.user.is_staff:
        compl_info=Complaint.objects.all()
        
    else:
        compl_info=Complaint.objects.filter(user=request.user)
    # compl_info=Complaint.objects.all()   
    data={
        'compl_info':compl_info,
    }
    return render(request,'my_complaint.html',data)


    

