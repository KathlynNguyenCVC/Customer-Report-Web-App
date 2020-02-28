from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['is_basic_report','owner','permission','file']





    
            



