from unicodedata import name
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("test_operations/",testone, name='shown'),
    path("shown/",shown, name='shown'),
    path("addpage/",addpage),
    path("viewpage/",viewpage, name="viewpage"),
    path("delete/<int:id>/",delete),
    path("viewpageone/<int:id>/",viewpageone),
    # path("viewpageone/<slug:slug>/",viewpageone),
    path("update/<int:id>/",update),
    path("updaterecord/<int:id>/",updaterecord),
    path("download_data/",download_data),
    path("download_single_data/<int:id>/",download_single_data),
    path("adminview/",adminview, name="adminview"),
    path("dateview/",dateview, name="dateview"),
    path("weekview/",weekview, name="weekview"),
    path("yearview/",yearview, name="yearview"),
    path("",loginpage, name="loginpage"),
    path("adminanduser/",adminanduser, name="adminanduser"),
    ] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
