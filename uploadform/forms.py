from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Report

PERMISSION_CHOICES = [
    ('FOLFER_TO_USER','Folder to User'),
    ('FOLDER_TO_GROUP','Folder to Group'),
    ('GROUP_TO_USER','Group to Folder')
]

class ReportForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ReportForm,self).__init__(*args,**kwargs)
      
        self.fields['owner'].required = False
    class Meta:
        model = Report
        fields = ['owner','is_basic_report','file','pivot_perm_folder_to_user','pivot_perm_folder_to_group','pivot_perm_group_to_user'] 





    
            



