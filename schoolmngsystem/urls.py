"""schoolmngsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import oec.views
import etechlab.views
import aet.views
import tss.views

from management import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index2', oec.views.index2, name='index2'),

    path('oec', oec.views.oec, name='oec'),

    path('morning', oec.views.morning, name='morning'),
    path('addaschool', oec.views.addaschool, name='addaschool'),
    path('schoollist', oec.views.schoollist, name='schoollist'),
    path('addaschoolupdate<str:pk>', oec.views.addaschoolupdate, name='addaschoolupdate'),
    path('editschool<str:pk>', oec.views.editschool, name='editschool'),

    path('deleteschool<str:pk>', oec.views.deleteschool, name='deleteschool'),


    # path('afternoon', oec.views.afternoon, name='afternoon'),

    path('etechlab', etechlab.views.etechlab, name='etechlab'),
    path('aet', aet.views.aet, name='aet'),
    path('tss', tss.views.tss, name='tss'),


]
