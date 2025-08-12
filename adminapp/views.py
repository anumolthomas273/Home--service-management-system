from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from adminapp.forms import category_Form
from django.contrib import messages

from homeapp.models import serviceprovider_Reg, user_Reg
from userapp.models import book, message

# Create your views here.
def index(request):
    return render(request,'admin/admin_index.html')

def addcategory(request):
    form=category_Form()
    if request.method == 'POST':  
        form = category_Form(request.POST)  
        if form.is_valid():  
            form.save() 
            messages.success(request, 'Added Successfull')

            return redirect('addcategory')
    return render(request,'admin/job category.html',{'form':form})

def service_pro(request):
    shop = serviceprovider_Reg.objects.filter(user__last_name='0',user__is_staff='0',user__is_active='1')
  
    return render(request,'admin/approve_service.html',{'shop':shop})


def approve(request,id):
    user = User.objects.get(pk=id)
    user.last_name='1'
    user.save()
    messages.success(request, 'Approved')

    return redirect('service_pro')

def reject(request,id):
    user = User.objects.get(pk=id)
    user.last_name='0'
    user.is_active='0'
    user.save()
    messages.success(request, 'Rejected')

    return redirect('service_pro')

def view_message(request):
    me=message.objects.all()

    if request.method=='POST':
        id=request.POST['id']
        reply=request.POST['reply']
        ch=message.objects.get(id=id)
        ch.reply=reply
        ch.save()
        messages.success(request, 'reply added')

        return redirect('/view_message')
        
    return render(request,'admin/view_message.html',{'me':me})
def view_user(request):
    shop = user_Reg.objects.all()
  
    return render(request,'admin/users.html',{'shop':shop})

def view_request_view(request):
    ch=book.objects.all()
    return render(request,'admin/view_request.html',{'ch':ch})