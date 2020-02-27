from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse


from .forms import UploadForm

def index(request):
    context={}
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'error':False,'message':'success'})
        else:
            return JsonResponse('error': True, 'errors': form.errors)
    else:
        form = UploadForm()
        context['form'] = form
        return render(request,'index.html',context)






