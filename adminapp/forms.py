from django.forms import ModelForm
from .models import job_category

class category_Form(ModelForm):
    class Meta:
        model=job_category
        fields=['job',]