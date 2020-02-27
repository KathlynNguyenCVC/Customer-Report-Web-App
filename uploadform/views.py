from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadForm

def index(request):
    context={}
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()
    context['form'] = form
    return render(request,'index.html',context)






