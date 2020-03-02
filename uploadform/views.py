from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache
import json


from .models import Report
from .forms import ReportForm

def upload_form(request):
    context = {}
    if request.method == 'POST':
        form = ReportForm(request.POST,request.FILES)
        form.is_basic_report = True if request.POST.get("report_type") == 'basic' else False
        form.permission = request.POST.get("permission")
        print(form.permission)
        form.owner = request.POST.get("owner")
        

        form.file = request.POST.get("file")
        print("file uploaded")
        ##print(form.file.content_type)
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message':form.errors})
    else: 
        form = ReportForm()
    context['form']=form
    return render(request,'upload_form.html',context)

def upload_status(request):
    if request.method == 'GET':
        if request.GET['key']:
            if cache.get(request.GET['key']):
                value = cache.get(request.GET['key'])
                return HttpResponse(json.dumps(value), content_type="application/json")
            else:
                return HttpResponse(json.dumps({'error':"No csrf value in cache"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'error':'No parameter key in GET request'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'error':'No GET request'}), content_type="application/json")








