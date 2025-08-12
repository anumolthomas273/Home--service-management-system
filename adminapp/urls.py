from django.urls import path

from adminapp import views



urlpatterns = [
    path('admin',views.index,name='admin'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('service_pro',views.service_pro,name='service_pro'),
    path('approve/<int:id>',views.approve,name='approve'),
    path('reject/<int:id>',views.reject,name='reject'),
    path('view_message',views.view_message,name='view_message'),
    path('view_request_view',views.view_request_view,name='view_request_view'),
    path('view_user',views.view_user,name='view_user'),





    
  
 
]
