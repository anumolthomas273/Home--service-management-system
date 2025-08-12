from django.db import models
from django.contrib.auth.models import User

from adminapp.models import job_category

# Create your models here.

    
    
class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)

class serviceprovider_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    LicenseNumber=models.CharField(max_length=200, null=True)
    Experience=models.CharField(max_length=200, null=True)
    Certifications=models.CharField(max_length=200, null=True)
    job=models.ForeignKey(job_category, on_delete=models.CASCADE, null=True)


    
class user_Reg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=200, null=True)
    