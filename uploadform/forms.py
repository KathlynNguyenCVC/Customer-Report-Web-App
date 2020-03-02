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
        #self.fields['permission']= forms.MultipleChoiceField(choices=PERMISSION_CHOICES, widget=forms.CheckboxSelectMultiple())
        #self.fields['permission'].initial = 'FOLFER_TO_USER'
        
        self.fields['permission'].required = False
        self.fields['owner'].required = False
    class Meta:
        model = Report
        fields = ['owner','permission','is_basic_report','file'] 





    
            



