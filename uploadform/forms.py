from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



class UploadForm(forms.Form):
    file = forms.FileField()

    basic = forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'checked': True}))
    pivot = forms.BooleanField(required=False)

    owner = forms.CharField(max_length=100,help_text='Owner Name')
    folder_to_user = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': True}),disabled=True)
    folder_to_group = forms.BooleanField(required=False)
    group_to_user = forms.BooleanField(required=False)


    
            



