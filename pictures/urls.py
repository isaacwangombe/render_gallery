from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path



urlpatterns=[
    url(r'^$',views.gallery, name ='gallery'),
    path('category/', views.category, name='category'),
    path('location', views.location, name='location'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)