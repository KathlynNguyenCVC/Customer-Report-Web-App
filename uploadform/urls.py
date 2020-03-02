from django.urls import path
from django.conf.urls import include, url

from . import views


urlpatterns = [
    path('', views.upload_form, name='upload-form'),
    url(r'^progressbarupload/?', include('progressbarupload.urls')),


]