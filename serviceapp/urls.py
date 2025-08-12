from django.urls import path

from serviceapp import views

urlpatterns = [
    path('service',views.index,name='service'),
    path('request',views.request,name='request'),
    path('approverequest/<int:id>',views.approverequest,name='approverequest')




  
 
]
