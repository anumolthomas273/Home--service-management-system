from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View

from homeapp.models import serviceprovider_Reg
from userapp.models import book

# Create your views here.
def index(request):
    return render(request,'service/index.html')

    
    
def request(request):
    us=serviceprovider_Reg.objects.get(user_id=request.user.id)
    ch=book.objects.filter(request='Requested',service_id=us.id)

    return render(request,'service/request.html',{'ch':ch})

def approverequest(request,id):
    user = book.objects.get(pk=id)
    user.request='Accepted'
    user.save()
    messages.success(request,'Accepted')
    return redirect('request')






