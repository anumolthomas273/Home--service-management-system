from django.urls import path

from userapp import views
from userapp.views import payment


urlpatterns = [
    path('user',views.index,name='user'),
    path('booking',views.booking,name='booking'),

    path('bookservice/<int:id>',views.bookservice,name='bookservice'),
    path('payment/<int:id>',views.payment,name='payment'),
    path('sendmessage',views.sendmessage,name='sendmessage'),

    path('view_reply',views.view_reply,name='view_reply'),


    
  
 
]
