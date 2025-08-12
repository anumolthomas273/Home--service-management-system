from django.db import models

from homeapp.models import serviceprovider_Reg, user_Reg


# Create your models here.
class book(models.Model):
    service = models.ForeignKey(serviceprovider_Reg, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(user_Reg, on_delete=models.CASCADE, null=True)
    time=models.CharField(max_length=200, null=True)
    date=models.CharField(max_length=200, null=True)
    status=models.CharField(max_length=200, null=True)
    payment=models.CharField(max_length=200, null=True)
    request=models.CharField(max_length=200, null=True)
    
    
class message(models.Model):
    user = models.ForeignKey(user_Reg, on_delete=models.CASCADE, null=True)
    subject=models.CharField(max_length=200, null=True)
    message=models.CharField(max_length=200, null=True)
    reply=models.CharField(max_length=200, null=True)