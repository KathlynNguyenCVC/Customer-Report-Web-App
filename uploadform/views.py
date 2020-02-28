from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.http import HttpResponse

from .models import Report
from .forms import ReportForm

def upload_form(request):
    context = {}
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        form.is_basic_report = True if request.POST.get("report_type") == 'basic' else False
        form.permission = request.POST.get("permission")
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message':form.errors})
    else: 
        form = ReportForm()
    context['form']=form
    return render(request,'upload_form.html',context)








