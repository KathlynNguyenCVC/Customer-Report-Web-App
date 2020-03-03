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
        if (form.is_basic_report):
            form.owner = request.POST.get("owner")
        if not (form.is_basic_report):
            form.pivot_perm_folder_to_user = True
            if (request.POST.get("folder_to_group")):
                form.pivot_perm_folder_to_group = True
            if (request.POST.get("group_to_user")):
                form.pivot_perm_group_to_user = True

        form.file = request.POST.get("file")
        uploaded_file = form.file
        fs = FileSystemStorage()
        file_name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(file_name)

        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
        else:
            return JsonResponse({'message':form.errors})
    else: 
        form = ReportForm()
    context['form']=form
    return render(request,'upload_form.html',context)


       








