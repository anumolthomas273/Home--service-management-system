from django.urls import path

from homeapp import views



urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.loginview,name='login'),
    path('user_registration',views.user_registration,name='user_registration'),
    path('register',views.register,name='register'),
    
  
 
]
