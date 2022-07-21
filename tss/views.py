from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView


def tss(request):
    return render(request,'tss/tss.html')
