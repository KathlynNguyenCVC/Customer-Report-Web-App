from django.urls import path
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import static
from django.conf import settings


from . import views

urlpatterns = [
    path('', views.upload_form, name='upload-form'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('handler/',views.handler,name='handler'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)