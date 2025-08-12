from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from adminapp.models import job_category
# from . models import Login,Registration
from homeapp.models import UserType, serviceprovider_Reg, user_Reg
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render(request,'index.html')



def loginview(request):
    if request.method=='POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('admin')
                elif UserType.objects.get(user_id=user.id).type == "service":
                    return redirect('service')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('user')
            else:
                messages.success(request,'User Account Not Authenticated')

                return render(request, 'login.html')
        else:
            messages.success(request,'Invalid Username or Password')

            return render(request, 'login.html')
    return render(request,'login.html')
    
    
def register(request):
    job=job_category.objects.all()
    
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        address = request.POST['address']
        certificate = request.POST['certificate']
        experience = request.POST['experience']
        category = request.POST['category']
        license = request.POST['license']

        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.success(request,'email already exist')

            return redirect('register')

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                         is_staff='0', last_name='0')
            user.save()
            us = serviceprovider_Reg()
            us.user = user
            us.LicenseNumber=license
            us.Experience=experience
            us.Certifications=certificate
            us.job_id=category
            us.phone = phone
            us.address = address
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "service"
            usertype.save()
            messages.success(request,'registration successful!')
            return redirect('login')
            
    return render(request,'register.html',{'job':job})




def user_registration(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phonenumber']
        address = request.POST['address']

        password = request.POST['password']
        if User.objects.filter(email=email):
            messages.success(request,'email already exist')

            return redirect('user_registration')

        else:
            user = User.objects._create_user(username=email, password=password, email=email, first_name=name,
                                         is_staff='0', last_name='1')
            user.save()
            us = user_Reg()
            us.user = user
            us.phone = phone
            us.address = address
            us.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            messages.success(request,'registration successful!')
            return redirect('login')
    
    return render(request,'user_reg.html')






