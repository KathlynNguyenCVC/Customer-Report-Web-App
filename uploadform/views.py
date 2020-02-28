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
        uploaded_file = request.FILES['']
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    else: 
        form = ReportForm()
    context['form']=form
    return render(request,'upload_form.html',context)

def report_list(request):
    reports = Report.objects.all()
    return render(request,'report_list.html',{'reports':reports})






