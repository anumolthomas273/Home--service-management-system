from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import messages

from homeapp.models import serviceprovider_Reg, user_Reg
from userapp.models import book, message

# Create your views here.
def index(request):
    ser=serviceprovider_Reg.objects.all()
    return render(request,'user/index.html',{'ser':ser})


def bookservice(request,id):
    if request.method=='POST':
        ser=serviceprovider_Reg.objects.get(id=id)
        us=user_Reg.objects.get(user_id=request.user.id)
        b=book()
        b.service_id=ser.id
        b.user_id=us.id
        b.time=request.POST['time']
        b.date=request.POST['date']
        b.status='book'
        b.payment='not Paid'
        b.request='Requested'

        b.save()
        return redirect('booking')


    
    return render(request,'user/book.html',)

def payment(request,id):
    if request.method=='POST':
        ch=book.objects.get(id=id)
        ch.payment='paid'
        ch.save()
        return redirect('/user')
        
    return render(request,'user/payment.html')

       

    
def booking(request):
    us=user_Reg.objects.get(user_id=request.user.id)
    ch=book.objects.filter(status='book',user_id=us)
    return render(request,'user/booking.html',{'ch':ch})


def sendmessage(request):
    if request.method=='POST':
        ch=message()
        us=user_Reg.objects.get(user_id=request.user.id)

        ch.subject=request.POST['subject']
        ch.message=request.POST['message']
        ch.user_id=us.id
        ch.reply='null'
        ch.save()
        messages.success(request, 'message Send')

        return redirect('sendmessage')
  
    return render(request,'user/message.html')


def view_reply(request):
    us=user_Reg.objects.get(user_id=request.user.id)
    ch=message.objects.filter(user_id=us)
    return render(request,'user/view_reply.html',{'me':ch})