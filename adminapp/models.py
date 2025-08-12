from django.db import models

# Create your models here.

class job_category(models.Model):
    job=models.CharField(max_length=200, null=True)