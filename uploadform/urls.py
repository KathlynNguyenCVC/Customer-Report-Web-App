from django.urls import path
from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('', views.upload_form, name='upload-form'),
    #path('uploadstatus',views.upload_status,name='upload-status'),


]